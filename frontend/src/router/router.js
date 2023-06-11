import {createRouter, createWebHistory} from "vue-router";
import VideoGrid from "@/components/VideoGrid.vue";
import RegistrationForm from "@/components/RegistrationForm.vue";
import DialogWindow from "@/components/DialogWindow.vue";


const routes = [
    {
        path: '/',
        component: VideoGrid
    },
    {
        path: '/account',
        component: RegistrationForm
    },
    {
        path: '/search?:req'
    },
    {
        path: '/register',
        component: DialogWindow
    },
    {
        path: '/auth',
        component: DialogWindow
    },
    {
        path: '/upload',
        component: DialogWindow
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})
export default router;