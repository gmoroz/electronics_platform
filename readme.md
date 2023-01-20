# Сайт объявлений

## Установка зависимостей и запуск проекта

Установка зависимостей через pip:

    python -m venv venv
    . env/bin/activate
    pip install -r requirements.txt

Установка зависимостей через poetry:

    poetry shell
    poetry install

Запуск проекта

    docker run --name elect -p 5432:5432 -e POSTGRES_PASSWORD=elect -e POSTGRES_USER=elect -e  POSTGRES_DB=elect -d postgres
    ./manage.py migrate
