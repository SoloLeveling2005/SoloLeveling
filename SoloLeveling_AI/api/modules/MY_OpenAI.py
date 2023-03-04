import json

import requests


def openAI_search_in_three_options(AI_TOKEN, message):
    """
    Принимает на вход сообщение на которое надо ответить
    Возвращает 3 варианта ответов на сообщение в ответ
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AI_TOKEN}"
    }
    assistant_answers = []

    # todo Вопрос юзера
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(url, headers=headers, json=data)
    answer_user = json.loads(response.text)['choices'][0]['message']['content']
    assistant_answers.append({f"{message}": answer_user})

    # todo Перефразированные вопросы
    # request = f"Измени формулировку запроса и вышли мне перефразированные 3 варианта в одной строке. раздели их тремя знаками процента без пояснений: {message}"
    #
    # history = [{"role": "user", "content": request}]
    #
    # data = {
    #     "model": "gpt-3.5-turbo",
    #     "messages": history
    # }
    # response = requests.post(url, headers=headers, json=data)
    # answer = (json.loads(response.text)['choices'][0]['message']['content']).split('%%%')
    #
    # # todo Задаем перефразированные вопросы
    # for i in answer:
    #     data = {
    #         "model": "gpt-3.5-turbo",
    #         "messages": [{"role": "user", "content": i}]
    #     }
    #     response = requests.post(url, headers=headers, json=data)
    #
    #     answer_child = json.loads(response.text)['choices'][0]['message']['content']
    #     assistant_answers.append({f"{i}": answer_child})

    return assistant_answers

