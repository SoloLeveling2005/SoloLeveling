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
# # print(tokenizer("Привет мир")['input_ids'])
# print(tokenizer("Hello world")['input_ids'])

# todo перевод текста
# import os
# import openai
#
# openai.api_key = "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"
#
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Write a small telegram bot on python.",
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
# answer = response['choices'][0]['text']
# print(answer)
# from googletrans import Translator
# translator = Translator()
# # translator.translate('안녕하세요.')
# code = answer
# print(translator.translate(code, dest='ru').text)
#
# import torch
# from transformers import AutoTokenizer, AutoModelForQuestionAnswering
#
# tokenizer = AutoTokenizer.from_pretrained("deepset/bert-base-cased-squad2")
# model = AutoModelForQuestionAnswering.from_pretrained("deepset/bert-base-cased-squad2")
#
# # Обучение модели на тексте
# text = "Jim Henson was a nice puppet"
# inputs = tokenizer(text, return_tensors="pt")
# with torch.no_grad():
#     outputs = model(**inputs)
#
# def answer_question(question, model, tokenizer):
#     inputs = tokenizer(question, text, return_tensors="pt")
#     with torch.no_grad():
#         outputs = model(**inputs)
#
#     answer_start_index = outputs.start_logits.argmax()
#     answer_end_index = outputs.end_logits.argmax()
#
#     predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
#     answer = tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)
#     return answer
#
# question = "Who was Jim Henson?"
# answer = answer_question(question, model, tokenizer)
# print(answer)
#
# question = "about whom?"
# answer = answer_question(question, model, tokenizer)
# print(answer)
import random
import json
import pickle
import numpy as np
import os
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import load_model
import random
import json

import pickle
import numpy as np

import nltk

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words( sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    p = bag_of_words(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.1
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(ints, intents_json):
    result = "I dont understand you"
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


while True:
    message = input("I: ")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)