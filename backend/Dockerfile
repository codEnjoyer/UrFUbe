FROM amd64/python:3.11.4-slim-bullseye

WORKDIR /fastapi_app/backend

COPY ./backend/requirements.txt /fastapi_app/backend

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r /fastapi_app/backend/requirements.txt

COPY ./backend /fastapi_app/backend

RUN chmod a+x ./docker/*.sh
