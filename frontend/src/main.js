import "bootstrap/dist/css/bootstrap.css"
import {createApp} from 'vue'
import App from './App'
import router from '@/router/router.js'
import store from '@/store'
import axios from "axios";

const app = createApp(App)

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      return router.push('/auth')
    } else if (error.response && error.response.status > 499) {
      originalRequest._retry = true;
      return router.push('/error')
    }
  }
});

app
    .use(router)
    .use(store)
    .use(require('vue-cookies'))
    .mount('#app')

axios.defaults.withCredentials = true;
//axios.defaults.baseURL = 'http://localhost:${BACK_PORT}/';
axios.defaults.baseURL = 'http://localhost:8000/';

import "bootstrap/dist/js/bootstrap.js"
