# Подключаем необходимые модули
from flask import Flask, render_template, redirect

# Создаем экземпляр приложения Flask
app = Flask(__name__)


# Создаем маршрут для главной страницы
@app.route('/')
def index():
    # Рендерим шаблон "index.html" и передаем в него данные
    # return render_template('index.html', title='Главная страница', message='Добро пожаловать!')

    return redirect("http://127.0.0.1:8000")
    # "http://127.0.0.1:8000"


# Запускаем сервер на порту 3000
if __name__ == '__main__':
    app.run(port=3000)
