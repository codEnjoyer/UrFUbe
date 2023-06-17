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
                        <button @click="add_like" class="btn likes">
                            <img src="../assets/likes.png">
                        </button>
                        <span style="margin-left: auto; margin-right: auto">{{ video.count_likes }}</span>
                    </div>
                    <div class="column_dir">
                        <button @click="add_dislike" class="btn dislikes">
                            <img src="../assets/dislikes.png">
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
                    <div class="btn sub" @click="post_comment">
                        <img class="icon-light" src="../assets/back.png" style="width: 32px">
                    </div>
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

.selected {
    filter: invert(100%);
}

.comment_form {
    display: flex;
    justify-content: space-around;
}

.sub {
    margin-top: auto;
    margin-bottom: auto;
}
</style>