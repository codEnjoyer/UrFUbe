# Видеохостинг **UrFUbe**

Техническая документация: [Google Docs](https://docs.google.com/document/d/1BYinXMtQc0jkYRjWXoz3YPrA6gg3O5Oc9XdZcPjQkGI/edit#).

Макет сайта: [Figma](https://www.figma.com/file/7A5t1IM5tEGZMcVlQ4ESKf/UrfuBe?type=design&node-id=0-1&mode=design&t=JoL46SMXIKPIQFsc-0).

## Быстрый старт:

* Перейти в корневую директорию проекта (UrFUbe/)
* Создать файл .env и заполнить его по примеру dev.env
* Выполнить команду:
```bash
docker compose up --build -d 
```

После запуска API проекта будет доступен по адресу: [http://localhost:{BACK_APP_PORT}/docs](http://localhost:8000/docs),
а фронтенд проекта будет доступен по адресу: [http://localhost:{FRONT_APP_PORT}](http://localhost:8080),
где {BACK_APP_PORT} и {FRONT_APP_PORT} - порты, указанные в файле .env

## Технологии, использующиеся в проекте
* Бэкенд-фреймворк - FastAPI
* Фронтенд-фреймворк - Vue.js
* База данных - PostgreSQL
* Миграции - Alembic
* ORM - SQLAlchemy
* Валидация - Pydantic
* Контейнеризация - Docker
* Система контроля версий - Git
* Облачное хранилище - Yandex Cloud Object Storage
* Хостинг - Yandex Cloud Compute Cloud
* Веб-сервер - Uvicorn
* Документация - Swagger
