import os

import discord
import requests
import json
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message)
    # quote = '/help'
    # await message.channel.send(quote)
    user = await client.fetch_user(9282)  # Замените USER_ID на ID пользователя, которому хотите отправить сообщение
    await user.send("Привет, это сообщение отправлено тебе в личку!")  # Отправляем сообщение пользователю

client.run(TOKEN)
