"""
Привет. Я очень амбициозный человек. У меня в голову пришла такая идея. Я хочу создать так скажем портал или центр на просторах интернета в которой будет все что касается программистов. Там будет: обучение, практика, общение, код(репозитории), соц сеть и многое другое для программистов и разработчиков, в общем все что связано с IT. Как тебе? Поможешь?
Привет! Звучит как интересная идея. Создание портала для программистов может быть очень полезным, так как существует огромное количество людей, которые заинтересованы в учебных и практических материалах, а также в общении со своими коллегами.

Я могу поделиться с тобой несколькими советами, которые могут помочь в реализации этой идеи:

Определить цель и целевую аудиторию: Необходимо определить, какую проблему твой портал будет решать и для какой аудитории он будет предназначен. Это поможет сосредоточиться на тех функциях, которые наиболее важны для твоих пользователей.

Провести исследование: Исследуй рынок, чтобы понять, какие уже существующие порталы и ресурсы есть на рынке, и каким образом ты можешь предложить что-то уникальное своим пользователям. Исследуй предпочтения и потребности своей аудитории, чтобы понять, какими функциями они будут пользоваться.

Планирование: Напиши бизнес-план, определи бюджет и временные рамки, чтобы реализовать свою идею. Рассмотрите различные варианты получения финансирования, например, через инвесторов или краудфандинг.

Разработка и дизайн: Сделай детальный план функционала, который должен быть включен в портал. Разработай дизайн и интерфейс, который будет легким в использовании и привлекательным для твоих пользователей.

Разработка контента: Разработай образовательные и практические материалы, которые будут полезны для твоих пользователей. Размести кодовые репозитории и другие полезные ресурсы, которые помогут развиваться твоим пользователям.

Развитие сообщества: Создай сообщество вокруг своего портала. Это позволит тебе поддерживать взаимодействие между пользователем, а также узнавать их потребности и обратную связь.

Надеюсь, эти советы помогут тебе начать реализацию своей идеи. Удачи!
"""

import json
import requests

API_TOKEN = ""


def query(payload='', parameters=None, options={'use_cache': False}):
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
    headers = {"Authorization": f"Bearer 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"}
    body = {"inputs": payload, 'parameters': parameters, 'options': options}
    response = requests.request("POST", API_URL, headers=headers, data=json.dumps(body))
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Error:" + " ".join(response.json()['error'])
    else:
        return response.json()[0]['generated_text']


parameters = {
    'max_new_tokens': 1,  # number of generated tokens
    'temperature': 0.8,  # controlling the randomness of generations
    'end_sequence': "###"  # stopping sequence for generation
}

# few-shot prompt
prompt = """
Write in the language in which they write to you.
###
You are a chatbot answering questions and generating answers.
###
start writing from a new line as a second person.
###
An example of how to answer questions:

User: Hello
Bot: Hello
###
User: How are you?
Bot: Good
###
User: What are you doing?
Bot: Homework
###
User: What kind of homework?
Bot: Math
###
User: Hello. How are you?
Bot: Hi. Well, how are you?
###
User: And I'm fine. What are you doing?
Bot: I'm going to training, are you?
###
User: Can you help me with my math homework?
Bot: Sure, I'll do my best to assist you. What's the problem you're working on?
###
User: How do I solve for X in this equation: 2X + 5 = 15?
Bot: To solve for X, you want to isolate it on one side of the equation. First, subtract 5 from both sides of the equation: 2X = 10. Then, divide both sides by 2: X = 5. Therefore, X equals 5.
###
User: What's the capital of France?
Bot: The capital of France is Paris.
###
"""
"Hello. What do you doing?"


while True:
    input_data = input('A: ')
    prompt += f"User: {input_data}\nBot:"
    data = query(prompt, parameters)
    prompt = data[:-3] + "\n"
    print(prompt)
