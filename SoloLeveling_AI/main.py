import json
import os
from datetime import datetime

from dotenv import load_dotenv
import telebot
import sqlite3
import openai
import requests

load_dotenv()

DB_ID_NOTION = os.getenv('DB_ID_NOTION')
NOTION_TOKEN = os.getenv('NOTION_TOKEN')

import os
from notionai import NotionAI

TOKEN = NOTION_TOKEN
SPACE_ID = DB_ID_NOTION
import requests
import json

url = "https://api.notion.com/v1/pages"
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2021-08-16"
}
payload = {
    "parent": { "database_id": DB_ID_NOTION },
    "properties": {
        "title": {
            "title": [
                {
                    "text": {
                        "content": "Yurts in Big Sur, California"
                    }
                }
            ]
        }
    }
}
response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.text)