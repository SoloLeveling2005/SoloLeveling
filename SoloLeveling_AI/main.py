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
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# add the EOS token as PAD token to avoid warnings
model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
from transformers import pipeline
# print(pipeline('sentiment-analysis')('we love you'))
input_ids = tokenizer.encode('Сколько будет 2+2', return_tensors='tf')

# generate text until the output length (which includes the context length) reaches 50
greedy_output = model.generate(input_ids, max_length=100)

# print("Output:\n" + 100 * '-')
print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))