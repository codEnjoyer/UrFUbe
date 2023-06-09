import {createRouter, createWebHistory} from "vue-router";
import VideoGrid from "@/components/VideoGrid.vue";
import RegistrationForm from "@/components/RegistrationForm.vue";


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
        path: '/search'
    },
    {
        path: '/register',
        component: RegistrationForm
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})
export default router;