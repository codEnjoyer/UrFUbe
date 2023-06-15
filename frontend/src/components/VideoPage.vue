<template>
  <div class="container">
    <video controls controlsList="nodownload" autoplay="autoplay" :key="video.id">
      <source ref="videoPlayer" src="" type="video/*">
    </video>
    <div class="video__text">
      <div>
        <h2 class="name">{{video.name}}</h2>
      </div>
      <div class="row">
        <router-link :to="'/account/' + video.user_id" class="username">{{video.username}}</router-link>
        <p class="username">Просмотры: {{video.watches}}</p>
      </div>
      <div>
        <p class="descr"> Описание: {{ video.description }}</p>
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

      }
    }
  },
  mounted() {
    // TODO: getVideo
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
  margin-right: 33%;
  margin-left: auto;
  max-width: 700px;
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
}
.row {
  display: flex;
  flex-direction: row;
}
.descr {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-decoration: none;
}
</style>