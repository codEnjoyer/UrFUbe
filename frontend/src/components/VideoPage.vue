<template>
    <div v-if="!is_load" class="container">
        <video controls controlsList="nodownload" autoplay="autoplay">
            <source ref="videoPlayer" :src="video.video_url">
        </video>
        <div class="video__text">
            <div>
                <h2 class="name">{{ video.name }}</h2>
            </div>
            <div class="row__dir">
                <router-link :to="'/account/' + video.user_id" class="username">{{ video.username }}</router-link>
                <div class="username" style="font-size: 16px">Просмотры: {{ video.count_views }}</div>
                <div v-if="$store.getters.is_authorised" class="reactions row__dir">
                    <div class="column_dir">
                        <button @click="add_like" class="btn">
                            <svg class="like"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M6.66662 10.3334V23.6667M6.66662 10.3334L1.33328 10.3333V23.6667H6.66662M6.66662 10.3334L13.5941 2.25132C14.2514 1.48442 15.2855 1.15474 16.2655 1.39972L16.3289 1.41557C18.1179 1.86284 18.9238 3.94745 17.901 5.48182L14.6666 10.3333H20.7471C22.4299 10.3333 23.6921 11.8728 23.3621 13.523L21.7621 21.523C21.5127 22.7695 20.4183 23.6667 19.1471 23.6667H6.66662"
                                    stroke="#303030" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>

                        </button>
                        <span style="margin-left: auto; margin-right: auto">{{ video.count_likes }}</span>
                    </div>
                    <div class="column_dir">
                        <button @click="add_dislike" class="btn">
                            <svg class="dislike"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M18.0814 14.6533L18.0814 1.31995M18.0814 14.6533L23.4147 14.6533L23.4147 1.31995H18.0814M18.0814 14.6533L11.1539 22.7353C10.4966 23.5022 9.46247 23.8319 8.48247 23.5869L8.41913 23.5711C6.63007 23.1238 5.8242 21.0392 6.847 19.5048L10.0814 14.6533H4.00087C2.31807 14.6533 1.05593 13.1138 1.38593 11.4637L2.98594 3.46368C3.23527 2.21715 4.32967 1.31995 5.60087 1.31995L18.0814 1.31995"
                                    stroke="#303030" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>

                        </button>
                        <span style="margin-left: auto; margin-right: auto">{{ video.count_dislikes }}</span>
                    </div>
                </div>
            </div>
            <div>
                <p class="descr"> Описание: {{ video.description }}</p>
            </div>
            <div class="comments_container">
                <h3>Комментарии</h3>
                <div v-if="$store.getters.is_authorised" class="comment_form">
                    <textarea v-model="text_comment" class="inp" type="text" placeholder="Комментарий"/>
                    <button class="btn submit-comment-button" @click="post_comment">
                        <svg width="50" height="50" viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M23.5926 7.4267L23.5908 7.42794C20.313 9.68657 15.3826 13.0973 11.2515 15.9606C9.18595 17.3922 7.32067 18.6866 5.96199 19.6315C5.28255 20.104 4.73035 20.4887 4.34331 20.7594C4.14963 20.8948 3.99831 21.001 3.89343 21.0751C3.80055 21.1407 3.76879 21.1641 3.76837 21.1635C3.76819 21.1633 3.77389 21.1586 3.78304 21.1508L3.77924 21.154C3.50609 21.3816 3.21037 21.8309 3.06934 22.3245L3.06816 22.3286C3.01927 22.497 3 22.5871 3 23.0014C3 23.2946 3.02043 23.4662 3.05686 23.6119C3.09394 23.7603 3.1595 23.9295 3.30159 24.2077C3.37728 24.3536 3.39449 24.392 3.41946 24.4244C3.43055 24.4389 3.44317 24.4521 3.46312 24.473C3.57615 24.5917 3.82253 24.8036 4.44911 25.2642C5.58759 26.1011 7.78425 27.6195 12.1928 30.667C12.5555 30.9177 12.9332 31.1788 13.3264 31.4506C16.1744 33.4181 18.8167 35.2419 20.6671 36.5191C22.1648 37.5529 23.1436 38.2285 23.2926 38.3323C23.9287 38.7697 24.1563 38.8685 24.3821 38.9263L24.3872 38.9276C25.1641 39.1307 25.9446 38.9151 26.5224 38.3241L26.5224 38.3241L26.5264 38.3201C26.8184 38.0247 27.0243 37.6759 27.1592 37.2273C27.1596 37.2258 27.1598 37.2248 27.1603 37.2222C27.1614 37.2161 27.1645 37.1975 27.1683 37.1581C27.1764 37.0733 27.1844 36.9292 27.1911 36.6628C27.2042 36.1332 27.2101 35.2107 27.2171 33.5069C27.2171 33.5068 27.2171 33.5067 27.2171 33.5066L27.2312 29.7944L27.235 28.7982H28.2312H28.6155C30.1457 28.7982 32.3854 29.1537 34 29.6425C35.5458 30.1083 37.3912 30.9406 38.7476 31.7723L38.7508 31.7742C42.0861 33.8366 44.7825 36.8051 46.5561 40.3227C46.6695 39.7249 46.76 39.1012 46.8354 38.409C46.8731 38.0619 46.8929 37.306 46.8876 36.492C46.8823 35.6797 46.8528 34.9084 46.8083 34.5329L46.808 34.5296C46.4976 31.8306 45.8558 29.6884 44.6858 27.4154C41.9289 22.0621 36.8409 18.3212 31.1158 17.4076L31.1137 17.4073C30.5001 17.308 29.4251 17.2045 29.1265 17.2045C28.9152 17.2045 28.6083 17.1888 28.4266 17.1723L28.4148 17.1712L28.4031 17.1698L28.1172 17.137L27.2346 17.0357L27.2312 16.1473L27.2171 12.4395L27.2037 8.89645L27.1446 8.72413L27.1445 8.72416L27.1404 8.71169C26.984 8.23522 26.8004 7.94316 26.5136 7.65579C26.1813 7.32753 25.9864 7.2062 25.6379 7.08471L25.6379 7.08476L25.6279 7.08113C25.5232 7.04338 25.4808 7.0337 25.433 7.02666C25.3654 7.0167 25.2596 7.00893 25.0198 7.00432L25.0117 7.00417L25.0037 7.00388C24.8263 6.99762 24.6929 6.99931 24.594 7.00549C24.4928 7.01181 24.4457 7.02181 24.4342 7.02473C24.1981 7.08529 23.8741 7.23181 23.5926 7.4267Z"
                                stroke-width="2"/>
                        </svg>
                    </button>
                </div>
                <div class="comment_cont" v-for="com in comments">
                    <hr>
                    <router-link :to="'/account/' + com.user_id" class="username">
                        {{ com.username }}
                    </router-link>
                    <p>
                        {{ com.text }}
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import videos from "@/store/modules/videos";
import {mapActions} from "vuex";

export default {
    name: "VideoPage",
    data() {
        return {
            video: {
                id: 0,
                name: '',
                username: '',
                count_likes: 0,
                count_dislikes: 0,
                description: '',
                count_views: 0,
                video_url: '',
                reaction_type_id: -1
            },
            comments: [],
            is_load: false,
            text_comment: '',
        }
    },
    async mounted() {
        this.is_load = true
        let r = await this.get_video({video_id: this.$route.params.video_id})
        if (r && r.status === 200) {
            this.video = r.data
        } else {
            this.$router.push('/error');
        }
        let r_com = await this.get_comments({video_id: this.$route.params.video_id})
        if (r_com && r_com.status === 200) {
            this.comments = r_com.data
        }
        this.username = (await this.account_me()).username;
        this.is_load = false
        console.log(this.video.reaction_type_id);
    },
    methods: {
        ...mapActions([
            'add_reaction', 'add_comment', 'get_comments', 'get_video', 'account_me'
        ]),
        async post_comment() {
            if (this.text_comment !== "") {
                await this.add_comment(
                    {
                        video_id: this.video.video_id,
                        text: this.text_comment
                    })
                this.comments.push({
                    video_id: this.video.video_id,
                    text: this.text_comment,
                    username: this.username
                })
                this.text_comment = "";
            }
        },
        async add_like() {
            let params = {
                video_id: this.video.video_id,
                reaction_type: 0
            }
            console.log(params);

            await this.add_reaction(params);
            if (this.video.reaction_type_id !== -1) {
                if (this.video.reaction_type_id === 1) {
                    this.video.count_dislikes -= 1
                    this.video.count_likes += 1
                    this.video.reaction_type_id = 0
                } else {
                    this.video.count_likes -= 1;
                    this.video.reaction_type_id = -1;
                }
            } else {
                this.video.reaction_type_id = 0;
                this.video.count_likes += 1;
            }
        },
        async add_dislike() {
            let params = {
                video_id: this.video.video_id,
                reaction_type: 1
            };
            console.log(params);
            await this.add_reaction(params);
            if (this.video.reaction_type_id !== -1) {
                if (this.video.reaction_type_id === 0) {
                    this.video.count_likes -= 1
                    this.video.count_dislikes += 1
                    this.video.reaction_type_id = 1
                } else {
                    this.video.count_dislikes -= 1;
                    this.video.reaction_type_id = -1;
                }
            } else {
                this.video.reaction_type_id = 1;
                this.video.count_dislikes += 1;
            }
            console.log(this.video.reaction_type_id);
        }
    }
}
</script>

<style scoped>
img {
    filter: var(--invert-light)
}

video {
    max-width: 800px;
    height: 450px;
    border-radius: 10px;
}

.container {
    margin-top: 30px;
    position: center;
    margin-right: auto;
    margin-left: 20%;
    max-width: 800px;
}

.username {
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-decoration: none;
    border-bottom: 0;
}

.username, .name, .username:hover {
    color: var(--color-text);
    text-decoration: none;
    width: 33%;
}

.row__dir {
    display: flex;
}

.reactions {
    margin-right: 0;
    margin-left: auto;
}

.btn, .btn:active {
    width: 50px;
    height: 50px;
    border-width: 0;
}

.column_dir {
    position: relative;
    display: flex;
    flex-direction: column;
    margin-right: 0;
    margin-left: auto;
}

.descr {
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-decoration: none;
}

.inp {
    font-size: large;
    margin: 20px;
    display: flex;
    flex-direction: row;
    padding: 10px 20px;
    gap: 20px;
    width: 90%;
    height: 100px;
    outline: none;
    overflow: hidden;

    background: var(--color-element);
    color: var(--color-text);
    border-radius: 10px;
    border-width: 0;

    resize: none;
}


.comment_form {
    display: flex;
    justify-content: space-around;
}

.submit-comment-button {
    margin: auto;
    padding: 0;
}

.submit-comment-button svg {
    stroke: var(--color-text);
    fill: none;
}

.submit-comment-button svg:hover {
    fill: var(--color-text);
}

.like, .dislike{
    fill: var(--background-color);
    stroke: var(--color-text);
    width: 25px;
    height: 25px;
}

.like:hover {
    fill: var(--color-success);
}

.dislike:hover {
    fill: var(--color-waiting);
}

</style>