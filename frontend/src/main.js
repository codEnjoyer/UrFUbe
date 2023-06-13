import "bootstrap/dist/css/bootstrap.css"
import { createApp } from 'vue'
// import axios from 'axios';
import App from './App'
import router from '@/router/router.js'
import store from '@/store'
import axios from "axios";

const app = createApp(App)

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      store.dispatch('logOut');
      return router.push('/login')
    }
  }
});

app
    .use(router)
    .use(store)
    .mount('#app')

// axios.defaults.withCredentials = true;
// axios.defaults.baseURL = 'http://localhost:${BACK_PORT}/';

import "bootstrap/dist/js/bootstrap.js"
