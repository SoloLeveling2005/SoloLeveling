# torch -> pip3 install --pre torch -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
# the package we'll use to send an HTTP request to Hugging Face's
# API
import json

from datasets import load_dataset

squad = load_dataset("squad", split="train[:5000]")

squad = squad.train_test_split(test_size=0.2)
datas = {'intents': [{
        'tag': data['title'] + "_" + data['id'][:10],
        'patterns': [data['question']],
        'responses': [data['answers']['text'][0]],
        "context_set": ""
    } for data in squad["train"]]}

with open('intents.json', 'w') as outfile:
    json.dump(datas, outfile)

# data = {
#     'id': '56cd687562d2951400fa6592',
#     'title': 'IPod',
#     'context': 'On January 8, 2004, Hewlett-Packard (HP) announced that they would sell HP-branded iPods under a license agreement from Apple. Several new retail channels were used—including Wal-Mart—and these iPods eventually made up 5% of all iPod sales. In July 2005, HP stopped selling iPods due to unfavorable terms and conditions imposed by Apple.',
#     'question': 'When did HP unveil their own edition of the iPod?',
#     'answers': {
#         'text': ['January 8, 2004'],
#         'answer_start': [3]
#     }
# }
