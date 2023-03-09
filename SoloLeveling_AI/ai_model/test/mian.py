# from transformers import pipeline

# image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# text = image_to_text("https://yandex-images.clstorage.net/5H1rsH168/423204DZ8b/rS7UgUVk0fpK_DKJa_NpqaUxKYyv6-kRNIHRmruh8s9f6cUQSpG8BNmIlZvS-LqvQ6InuR1M55gDZo7n8xGASe55mc0OJ8auHL4s3WPwbKu4bGqds7HtTC7DjZH__qTLV-zXR0KD4lLDzcyauMHL3mWeX9ljM5zjG2WDu6ZanhGhEP_ARF-N32vKfaRQ0lWluncVoq2d5nYXqZ2YwICSpi-Zt0RXip5j8OyDzJ_TwPlSt2rqbSCz6AFznYa0deo8iQnLkFZ2mfBY6FK-UvFqlrNVBp6yjfJoPqGcrOy2u5srrp92VZqLf-rxiOmv-vz1ZZVx8VozrMkucIqXt2r_HpQ15rBuR4rxVMF0qFjUS5yzejCAq4PafzuGhZf1t6WsFY2iRW22rGD-1Yv6iPff71CSUd1JMrzvME-cmrN70gu-P8KwRX637WPIeYhn9ni8tnQQnK-Q4nYWrr6x-aeytSG6oUtAn5ZPwsWG4pDWyPxgonj-Riyd6ilXuZqGYfI2qCT4knFPp81GwHKheehlm616Kp-xq_dhJ7CtneKCpZ4HvrtFVp6Re9TXiOmQ7_v2Uph5z1ocneoodYW5rGjeHr4cwYtlY4zcXcR_l0jcWYCPdSKzoZ7nfBaOjbXgtI-_I6mIdkicqGP3-ITckefo0UWVZtJ7O5v9M2Whhrpw6RutB-ehc0CN_1rBaYdA-nW8jnIthr2Dymgyh6Ce54efjCqKuGlCmLFw-M2XyY_QyNxLslTbQRaM-TBQha6hTf4iqQLikmdkh-FDxUuZQ_hLtbZTCoaptuZYDamohuWqnbUenoFfXICuZ8nOu82TyevYSIl4_VIFmv4haL6srGnUKJc34pF5bbHGa-hJoW7vQ4moSSmbuK32ZhmMvLDAlZKTFqu-XEKBoU7Dy4fOlOzc0kOZftJNAZbpEW-grqFP4SqqKOaKWm6Q4H_1SoZO3kmZhXgyrYqe9HY4rI-U9ak")
# print(text)

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    LogitsProcessorList,
    MinLengthLogitsProcessor,
    BeamSearchScorer,
)
import torch

tokenizer = AutoTokenizer.from_pretrained("t5-base", cache_dir="./")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base", cache_dir="./")

encoder_input_str = """
Сократи.

Алекса́ндр Македо́нский (Александр III Великий, др.-греч. Ἀλέξανδρος Γ' ὁ Μέγας; предположительно 20/23 июля или 6/10 октября 356 года до н. э., Пелла — 10/13 июня 323 года до н. э., Вавилон) — царь Древней Македонии из династии Аргеадов (с 336 года до н. э.), выдающийся полководец, создатель мировой державы, распавшейся после его смерти.

После гибели своего отца, Филиппа II, Александр в возрасте 20 лет был объявлен царем. Он подавил восстание фракийцев и заново подчинил Грецию, где были разрушены мятежные Фивы. В 334 году до н. э. Александр переправился в Малую Азию, начав таким образом войну с Персидской державой. При Гранике он разгромил сатрапов, а при Иссе (333 год до н. э.) — самого царя Дария III, после чего подчинил Сирию, Палестину и Египет. В 331 году до н. э. при Гавгамелах в Месопотамии Александр одержал решающую победу. Дарий позже был убит; Александр, заняв внутренние районы Персии, принял титул «царь Азии», окружил себя представителями восточной знати и начал думать о завоевании мира. За три года (329—326 годы до н. э.) он завоевал Среднюю Азию, а потом вторгся в Индию, но утомлённое войско отказалось идти дальше. Александр повернул назад и в 324 году до н. э. прибыл в Вавилон, ставший его столицей. В следующем году, во время подготовки к походу в Аравию, Александр умер в возрасте тридцати двух лет.

Созданная в ходе завоеваний держава вскоре распалась, разделённая между полководцами царя — диадохами. Тем не менее благодаря походам Александра началось распространение греческой культуры на Востоке, заложившее основу эллинизма.

Александр ещё в античную эпоху был признан одним из величайших полководцев в истории. Его имя активно использовалось в политической пропаганде. В Средние века одной из самых популярных книг в Европе и ряде регионов Азии и Африки стал «Роман об Александре», наполнивший биографию заглавного героя вымышленными эпизодами; в мусульманской традиции Александра начали отождествлять с Зу-ль-Карнайном. В эпоху барокко македонский царь стал популярным персонажем театра и живописи.


"""
encoder_input_ids = tokenizer(encoder_input_str, return_tensors="pt").input_ids


# lets run beam search using 3 beams
num_beams = 3
# define decoder start token ids
input_ids = torch.ones((num_beams, 1), device=model.device, dtype=torch.long)
input_ids = input_ids * model.config.decoder_start_token_id

# add encoder_outputs to model keyword arguments
model_kwargs = {
    "encoder_outputs": model.get_encoder()(
        encoder_input_ids.repeat_interleave(num_beams, dim=0), return_dict=True
    )
}

# instantiate beam scorer
beam_scorer = BeamSearchScorer(
    batch_size=1,
    num_beams=num_beams,
    device=model.device,
)

# instantiate logits processors
logits_processor = LogitsProcessorList(
    [
        MinLengthLogitsProcessor(5, eos_token_id=model.config.eos_token_id),
    ]
)

outputs = model.beam_search(input_ids, beam_scorer, logits_processor=logits_processor, **model_kwargs)

tet = tokenizer.batch_decode(outputs, skip_special_tokens=True)
print(tet)