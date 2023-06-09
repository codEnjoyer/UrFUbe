FROM python:3.11

WORKDIR /fastapi_app

COPY ./requirements.txt /fastapi_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi_app/requirements.txt

COPY . /fastapi_app

RUN chmod a+x docker/*.sh
