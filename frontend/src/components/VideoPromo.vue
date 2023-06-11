<template>
 <div  class="container__video">
   <div class="preview__wrap">
     <img @click="watch_video" :src="pre" class="preview">
     <router-link to="/search" @click="watch_video" class="name">
       <a>{{name}}</a>
     </router-link>
     <router-link :to="'/user/' + user_id">
       <a class="username">{{user_name}}</a>
     </router-link>
   </div>
 </div>
</template>

<script>
export default {
  name: "video-promo",
  props: {
    preview: { type: String, default: 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png' },
    name: { type: String, default: 'Очень крутое видео, посмотрите какие круты е котята, очень классные котята, самое милое видео навсегда' },
    user_id: { type: Number, default: 0 },
    user_name: { type: String, default: "aynjysadasdf sdasdasdasdasdasddddddddddddddsdf ddddddddasddddddd dddddddddddddd"}
  },
  data() {
    return {
      pre: require('../assets/video/default_preview.png')
    }
  },
  mounted() {
    this.pre = this.preview;
  },
  methods: {
    watch_video() {
      this.$router.push('/search');
    }
  }
}
</script>

<style scoped>
.container__video {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 0px;
  gap: 19px;

  width: 344px;
  height: 293px;
}
.preview__wrap {
  width: 344px;
  height: 200px;
  background-color: var(--background-color);
  border-radius: 10px;
}
.preview {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  text-overflow: ellipsis;
}
</style>