<template>
  <div class="container">
    <video controls controlsList="nodownload" autoplay="autoplay" :key="video.id">
      <source ref="videoPlayer" src="" type="video/*">
    </video>
    <div class="video__text">
      <div>
        <h2 class="name">{{video.name}}</h2>
      </div>
      <div class="row__dir">
        <router-link :to="'/account/' + video.user_id" class="username">{{video.username}}</router-link>
        <div class="username" style="font-size: 16px">Просмотры: {{video.watches}}</div>
        <div class="reactions row__dir">
          <div class="column_dir">
            <button @click="add_like" class="btn likes">
              <img src="../assets/likes.png">
            </button>
            <span style="margin-left: auto; margin-right: auto">{{video.likes}}</span>
          </div>
          <div class="column_dir">
            <button @click="add_dislike" class="btn dislikes">
              <img src="../assets/dislikes.png">
            </button>
            <span style="margin-left: auto; margin-right: auto">{{video.dislikes}}</span>
          </div>
        </div>
      </div>
      <div>
        <p class="descr"> Описание: {{ video.description }}</p>
      </div>
      <div class="comments_container">
        <div class="comment_form">
          <textarea class="inp" type="text" placeholder="Комментарий" />
          <div class="btn sub" @click="add_comment">
            <img class="icon-light" src="../assets/back.png" style="width: 32px">
          </div>
        </div>
        <div class="comment_cont" v-for="com in comments">
          <hr>
          <router-link :to="'/user/' + com.user_id" class="username">{{com.username}}</router-link>
          <p>{{com.text}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "VideoPage",
  data() {
    return {
      video: {
        username: "dsfsdfsdfsdf",
        likes: 0,
        dislikes: 0,
        watches: 100000
      },
      comments: []
    }
  },
  mounted() {
    // TODO: getVideo
    // TODO: getComments
  },
  methods: {
    add_comment() {
      // TODO: addComment
    },
    add_like() {
      // TODO: addlike
    },
    add_dislike() {
      // TODO: addDislike
    }
  }
}
</script>

<style scoped>
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
.column_dir{
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
  outline:none;
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