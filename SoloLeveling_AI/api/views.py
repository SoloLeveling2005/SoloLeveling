import json

from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import json
import os
from dotenv import load_dotenv
import sqlite3
import openai
import requests
from api import models

load_dotenv()

TOKEN = os.getenv('TOKEN')
AI_TOKEN = os.getenv('AI_TOKEN')


def openAI(history, message):
    # print(history)
    history.append({"role": "user", "content": message})

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AI_TOKEN}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": history
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.text)
    assistant_answer = json.loads(response.text)['choices'][0]['message']['content']

    history.append({"role": "assistant", "content": assistant_answer})
    return history, assistant_answer

# Create your views here.

@api_view(http_method_names=["POST", "GET"])
@permission_classes((permissions.AllowAny,))
def request_ai(request):
    global assistant_answer
    user = models.User.objects.get(id=1)

    if request.method == "POST":
        user_message = request.data['message']
        try:
            request_data = models.Room.objects.get(user_id=user).data
            data = [i for i in json.loads(request_data)['data']]
            # data.append(user_message)
            history, assistant_answer = openAI(data, user_message)

            # todo замена
            request_data = models.Room.objects.get(user_id=user)
            request_data.data = json.dumps({'data': history})
            request_data.save()

        except Exception as e:
            print(e)
            history, assistant_answer = openAI([], user_message)
            request_data = models.Room.objects.create(user_id=user,
                                                                  data=json.dumps({'data': history}))
            request_data = request_data.data
            data = [i for i in json.loads(request_data)['data']]

        OpenAI = ""
        YouChat = ""
        print(assistant_answer)
        return Response(data={'data': {'OpenAI': assistant_answer, 'YouChat': YouChat}}, status=status.HTTP_200_OK)
    else:
        try:
            request_data = models.Room.objects.get(user_id=user).data
            data = [i for i in json.loads(request_data)['data']]
        except Exception as e:
            print(e)
            data = []
        # openAI(data, "Hello")
        return Response(data={'data': data}, status=status.HTTP_200_OK)
#     {"message":"123"}



def openAI_search(message):
    """
    Принимает на вход сообщение на которое надо ответить
    Возвращает сообщение ответ
    """

    history = [{"role": "user", "content": message}]

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AI_TOKEN}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": history
    }

    response = requests.post(url, headers=headers, json=data)

    assistant_answer = json.loads(response.text)['choices'][0]['message']['content']

    return assistant_answer

@api_view(http_method_names=["POST", "GET"])
@permission_classes((permissions.AllowAny,))
def search(request):

