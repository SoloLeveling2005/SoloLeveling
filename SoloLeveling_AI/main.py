# import json
# import os
# from datetime import datetime
#
# from dotenv import load_dotenv
# import telebot
# import sqlite3
# import openai
# import requests
#
# load_dotenv()
#
# DB_ID_NOTION = os.getenv('DB_ID_NOTION')
# NOTION_TOKEN = os.getenv('NOTION_TOKEN')
#
# import os
# from notionai import NotionAI
#
# TOKEN = NOTION_TOKEN
# SPACE_ID = DB_ID_NOTION
# import requests
# import json
#
# url = "https://api.notion.com/v1/pages"
# headers = {
#     "Authorization": "Bearer " + NOTION_TOKEN,
#     "Content-Type": "application/json",
#     "Notion-Version": "2021-08-16"
# }
# payload = {
#     "parent": { "database_id": DB_ID_NOTION },
#     "properties": {
#         "title": {
#             "title": [
#                 {
#                     "text": {
#                         "content": "Yurts in Big Sur, California"
#                     }
#                 }
#             ]
#         }
#     }
# }
# response = requests.post(url, headers=headers, data=json.dumps(payload))
#
# print(response.text)

# from transformers import pipeline
#
# text_generation = pipeline("text-generation")
# generated_text= text_generation("Hello.", max_length=50, do_sample=False)[0]
#
# print(generated_text["generated_text"])


# from transformers import pipeline
# question_answering = pipeline("question-answering")
# context = """
# Следующим ханом, сумевшим за 30 лет правления возродить и усилить Казахское ханство, был сын Касыма - хан Хакназар. Он прославился не только патриотизмом, но и перевербовкой своих противников.  Пока господствовали Тахир и Буйдаш, Хакназар жил у одного из ногайских мурз. Мангыты во время казахских междоусобиц были едины и сильны, пытались навязать казахам свою политику. Но свободолюбивые казахские султаны не желали подчиняться, ни силе, ни золоту. Тогда ногайские мурзы решили использовать хана Хакназара, популярного, как среди мангытов, так и среди казахов. Обещая содействие, он перевербовал мангытов, победил в междоусобице и объединил казахов. Часть ногайцев вошла в состав Младшего жуза, расширив западные границы. Остальных он вынудил перекочевать далее к реке Дон.  Во внешней политике Хакназар наладил дипломатические и торговые отношения с Москвой при Иване IV Грозном (1547 -1584 гг.). Например, купцам Строгоновым была выдана грамота на беспошлинную торговлю с казахами. В 1559 г. вместе с послами из Бухары Балха и Ургенча приехал английский купец Энтони Дженкинсон. К нам в 1569-1573 гг. прибыли послы Семен Мальцев и Третьяк Чебуков. Москвичам нужна была наша помощь в борьбе с ханом Сибири Кучумом. Поддерживался союз с башкирами и киргизами. Бывших противников узбеков-шайбанидов Хакназар так же перевербовал, подписав «клятвенный союз» с ханом Бухары Абадаллахом II, чем значительно укрепил экономику ханства.  Неудачно складывались отношения с моголами Абд ар-Рашида и ойратами. Было разорена и потеряна Восточная часть Семиречья. Да и Сибирское ханство периодически беспокоило северные границы. После распада Ногайской орды нашими соседями стали русские. А после нашей помощи казачьему атаману Ермаку Тимофеевичу в покорении столицы Сибири города Кашлыка, хан Кучум и вовсе перестал беспокоить. Со временем многие сибирские племена войдут в состав Казахского ханства.
#
# """
# question = "В каком годе к нам прибыли послы Семен Мальцев и Третьяк Чебуков"
# result = question_answering(question=question, context=context)
#
# print("Answer:", result['answer'])
# print("Score:", result['score'])
# print(result)


# import torch
# from transformers import GPT2TokenizerFast
#
# tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
# print(tokenizer("Привет мир")['input_ids'])
# print(tokenizer("Hello world")['input_ids'])

import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a small telegram bot on python.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
answer = response['choices'][0]['text']
print(answer)
from googletrans import Translator
translator = Translator()
# translator.translate('안녕하세요.')
code = answer
print(translator.translate(code, dest='ru').text)


