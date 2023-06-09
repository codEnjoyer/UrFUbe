import "bootstrap/dist/css/bootstrap.css"
import { createApp } from 'vue'
import App from './App'
import router from '@/router/router.js'

const app = createApp(App)
app
    .use(router)
    .mount('#app')

import "bootstrap/dist/js/bootstrap.js"
