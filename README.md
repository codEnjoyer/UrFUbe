# Видеохостинг [UrFUbe](http://158.160.109.150:8080)

Документация на хостинге [здесь](http://158.160.109.150:8000/docs)

Техническая документация: [Google Docs](https://docs.google.com/document/d/1BYinXMtQc0jkYRjWXoz3YPrA6gg3O5Oc9XdZcPjQkGI/edit#).

## Быстрый старт:

* Перейти в корневую директорию проекта (UrFUbe/)
* Создать файл .env и заполнить его по примеру dev.env
* Выполнить команду:
```bash
docker compose up --build -d 
```

API также доступен по адресу: http://localhost:{BACK_APP_PORT}/docs

## Технологии, использующиеся в проекте
* Система контроля версий - Git
* Фронтенд-фреймворк - Vue.js
* Бэкенд-фреймворк - FastAPI
* Облачное хранилище - Yandex Cloud Object Storage
* Хостинг - Yandex Cloud Compute Cloud
* Контейнеризация - Docker
* База данных - PostgreSQL
* Язык программирования - Python
* Веб-сервер - Uvicorn
* Асинхронность - asyncio
* ORM - SQLAlchemy
* Миграции - Alembic
* Валидация - Pydantic
* Документация - Swagger
