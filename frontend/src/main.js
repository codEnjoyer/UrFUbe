import "bootstrap/dist/css/bootstrap.css"
import { createApp } from 'vue'
// import axios from 'axios';
import App from './App'
import router from '@/router/router.js'

const app = createApp(App)
app
    .use(router)
    .mount('#app')

// axios.defaults.withCredentials = true;
// axios.defaults.baseURL = 'http://localhost:${BACK_PORT}/';

import "bootstrap/dist/js/bootstrap.js"
