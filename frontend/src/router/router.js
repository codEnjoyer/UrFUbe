import {createRouter, createWebHistory} from "vue-router";
import VideoGrid from "@/components/VideoGrid.vue";
import VideoList from "@/components/VideoList.vue";
import UploadForm from "@/components/forms/UploadForm.vue";
import AccountPage from "@/components/AccountPage.vue";
import VideoPage from "@/components/VideoPage.vue";
import DialogWindow from "@/components/DialogWindow.vue";
import MyVideoPage from "@/components/MyVideoPage.vue"


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
        path: '/account/me',
        component: MyVideoPage
    },
    {
        path: '/video/:video_id',
        component: VideoPage
    },
    {
        path: '/search/:req',
        name: 'search',
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
    },
    {
        path: '/error',
        component: VideoGrid
    }
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})
export default router;