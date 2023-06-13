<template>
  <div class="video__promo">
    <router-link :to="'/video/' + video.user_id" class="preview">
      <img :src="pre" >
    </router-link>
    <div class="video__text">
      <router-link :to="'/video/' + video.user_id" style="text-decoration: none; color: inherit;">
        <a class="name">
          <p>{{video.name}}</p>
        </a>
       </router-link>
       <router-link :to="'/user/' + video.user_id" class="username">
         <p> Автор: {{video.username}} </p>
       </router-link>
     <p class="username">Просмотры: {{video.watches}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "VideoPromoHorizontal",
  props: {
    video: { type: Object, required: true }
  },
  data() {
    return {
      pre: require('../assets/video/default_preview.png'),
      video: {
        preview: "https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_92x30dp.png",
        name: "asdaaaaaaaaaaaaaaaaaaaaaaaaaaaa asdaaaaaaaaask askdasdaskdk askdkaskd",
        username: 'jsdfjsdjfsjdf jsdfjsdjfjsdfj sdjfsjdfjsj dsjfjsdfj jsdjfsjdf j',
        watches: 100000000,
        video_id: 0,
        user_id: 0
      }
    }
  },
  mounted() {
    if (this.video.preview) {
      this.pre = this.video.preview;
    }
  }
}
</script>

<style scoped>
.video__promo {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: 0;
  margin-bottom: 30px;
}
.preview img {
  width: 172px;
  height: 100px;
  object-fit: cover;
  margin: 20px 30px;
  overflow: hidden;
}
.name {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 18px;
  text-transform: uppercase;
  text-align: inherit;
  margin-bottom: 0;
}
.username {
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 18px;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-decoration: none;
  border-bottom: 0;
}
.username, .name, .username:hover, .name:hover, .name:active, .name:focus {
  color: var(--color-text);
  text-decoration: none;
}
</style>