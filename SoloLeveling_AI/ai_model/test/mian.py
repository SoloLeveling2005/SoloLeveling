from transformers import GPTNeoForCausalLM, GPT2Tokenizer, AutoModelForCausalLM, AutoModel
import torch

model_name = "EleutherAI/gpt-neo-2.7B"

model = AutoModel.from_pretrained(model_name, use_auth_token=False)

free_vram = 0.0
if torch.cuda.is_available():
    from pynvml import *
    nvmlInit()
    h = nvmlDeviceGetHandleByIndex(0)
    info = nvmlDeviceGetMemoryInfo(h)
    free_vram = info.free/1048576000
    print("There is a GPU with " + str(free_vram) + "GB of free VRAM")
if model_name == "Eleuthera/gpt-neo-2.7B" and free_vram>13.5:
    use_cuda = True
    model.to("cuda:0")
elif model_name == "Eleuthera/gpt-neo-1.3B" and free_vram>7.5:
    use_cuda = True
    model.to("cuda:0")
else:
    use_cuda = False

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
prompt = str(input("Write:"))

output_length = 200

input_ids = tokenizer(prompt, return_tensors="pt").input_ids
if use_cuda:
    input_ids = input_ids.cuda()

get_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=output_length)
get_text = tokenizer.batch_decode(get_tokens)[0]
print(get_text)


