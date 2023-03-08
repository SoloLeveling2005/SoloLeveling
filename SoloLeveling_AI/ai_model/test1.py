from transformers import pipeline

question = "Базовая маршрутизация"
context = """
Базовая маршрутизация
Самые простые маршруты Laravel принимают URI и замыкание, предоставляя очень простой и выразительный метод определения маршрутов и поведения без сложных файлов конфигурации маршрутизации:

use Illuminate\Support\Facades\Route;
 
Route::get('/greeting', function () {
    return 'Hello World';
});
"""
question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad",)

while True:
    question = input('what: ')
    print(question_answerer(question=question, context=context))