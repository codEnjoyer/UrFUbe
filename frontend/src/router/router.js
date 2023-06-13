import {createRouter, createWebHistory} from "vue-router";
import VideoGrid from "@/components/VideoGrid.vue";
import RegistrationForm from "@/components/forms/RegistrationForm.vue";
import DialogWindow from "@/components/DialogWindow.vue";
import VideoList from "@/components/VideoList.vue";
import UploadForm from "@/components/forms/UploadForm.vue";
import AccountPage from "@/components/AccountPage.vue";
import VideoPage from "@/components/VideoPage.vue";


const routes = [
    {
        path: '/',
        component: VideoGrid
    },
    {
        path: '/account/:user_id',
        component: AccountPage
    },
    {
        path: '/video/:video_id',
        component: VideoPage
    },
    {
        path: '/search/:req',
        component: VideoList
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
        component: UploadForm
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})
export default router;