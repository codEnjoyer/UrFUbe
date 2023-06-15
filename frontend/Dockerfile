FROM node:lts-alpine3.18

WORKDIR /fastapi_app/frontend

RUN npm install @vue/cli@5.0.8 -g

COPY package.json .

COPY package-lock.json .

RUN npm install

RUN npm run serve