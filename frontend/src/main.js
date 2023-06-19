import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap.js"
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
    } else {
      return error
    }
  }
});

app
    .use(router)
    .use(store)

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

app.mount('#app')
