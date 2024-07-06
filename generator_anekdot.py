import requests
from googletrans import Translator


def get_random_joke():
    # Создаем экземпляр класса Translator
    translator = Translator()

    # URL для получения случайной шутки
    url = "https://v2.jokeapi.dev/joke/Any"

    # Отправляем GET-запрос к API
    response = requests.get(url)

    # Проверяем, успешно ли выполнен запрос
    if response.status_code == 200:
        # Если запрос успешен, преобразуем ответ в формат JSON
        joke_data = response.json()

        # Проверяем тип шутки: если шутка однострочная
        if joke_data["type"] == "single":
            # Переводим шутку на русский язык
            joke = translator.translate(joke_data["joke"], dest='ru')
            # Выводим переведенную шутку
            print(joke.text)

        # Если шутка двухчастная
        elif joke_data["type"] == "twopart":
            # Переводим начало шутки на русский язык
            setup = translator.translate(joke_data["setup"], dest='ru')
            # Переводим окончание шутки на русский язык
            delivery = translator.translate(joke_data["delivery"], dest='ru')
            # Выводим переведенное начало шутки
            print(setup.text)
            # Выводим переведенное окончание шутки
            print(delivery.text)
    else:
        # Если запрос не удался, выводим сообщение об ошибке
        print("Не удалось получить шутку, попробуйте позже.")


if __name__ == "__main__":
    get_random_joke()
