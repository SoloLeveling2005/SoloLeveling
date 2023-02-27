import os
from dotenv import load_dotenv
import telebot
import sqlite3

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

with sqlite3.connect("tasks.db") as cur:
    res = cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_chat_id VARCHAR(255),
        text VARCHAR(255)
        );
        """)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать!")


@bot.message_handler(commands=['create_task'])
def send_welcome(message):
    new_task(message)


@bot.message_handler(func=lambda message: True)
def main(message):
    if message.text == "Добавь задачу":
        new_task(message)
    elif message.text == "Выведи все задачи":
        get_all_tasks(message)
    else:
        bot.send_message(message.chat.id, 'Не понял ваш запрос')


def new_task(message):
    msg = bot.send_message(message.from_user.id, 'Введите название задачи: ')
    bot.register_next_step_handler(msg, new_task_step_2)


def new_task_step_2(message):
    with sqlite3.connect("tasks.db") as cur:
        cur.execute(f"""
            INSERT INTO tasks (text) VALUES ('{message.text}');
        """)
    bot.send_message(message.chat.id, 'Задача добавлена')


def get_all_tasks(message):
    with sqlite3.connect("tasks.db") as cur:
        res = cur.execute(f"""
            SELECT * FROM tasks;
        """)
        data = res.fetchall()

    if data:
        bot.send_message(message.chat.id, 'Ваши задачи:')
        for i in data:
            print(i)
            bot.send_message(message.chat.id, i[2])
    else:
        bot.send_message(message.chat.id, "У вас нет задач")

if __name__ == "__main__":
    print("Start bot")
    bot.infinity_polling()
