FROM python:3.11

WORKDIR /fastapi_app/backend

COPY ./backend/requirements.txt /fastapi_app/backend

RUN pip install --upgrade pip

RUN pip install -r /fastapi_app/backend/requirements.txt

COPY ./backend /fastapi_app/backend

RUN chmod a+x ./docker/*.sh
