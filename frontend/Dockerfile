FROM node:lts-alpine3.18 as build-stage

WORKDIR /fastapi_app/frontend

RUN npm install @vue/cli@5.0.8 -g

COPY package.json .

COPY package-lock.json .

RUN npm install

COPY . .

#RUN npm run serve
CMD ["npm", "run", "serve"]
#
#FROM nginx:stable-alpine as production-stage
#COPY --from=build-stage /fastapi_app/frontend/dist /usr/share/nginx/html
#EXPOSE 8000
#CMD ["nginx", "-g", "daemon off;"]