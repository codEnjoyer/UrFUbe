<template>
 <div  class="container__video">
   <div class="preview__wrap">
     <router-link :to="'/video/' + user_id" style="text-decoration: none; color: inherit;">
       <img :src="pre" class="preview">
       <a class="name">
         <p>{{name}}</p>
       </a>
     </router-link>
     <router-link :to="'/user/' + user_id" class="username">
       <p> Автор: {{user_name}} </p>
     </router-link>
     <p class="username">Просмотры: {{watches.toString()}}</p>
   </div>
 </div>
</template>

<script>
export default {
  name: "video-promo",
  props: {
    preview: { type: String, default: 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png' },
    name: { type: String, default: 'Очень крутое видео, посмотрите какие круты е котята, очень классные котята, самое милое видео навсегда' },
    video_id: { type: Number, default: 0 },
    user_id: { type: Number, default: 0 },
    user_name: { type: String, default: "sdasdasdasdasdasddd dddddddddddsdfфывфывфывфв ddddddddasddddddd dddddddddddddd"},
    watches: { type: Number, default: 10000000000 }
  },
  data() {
    return {
      pre: require('../assets/video/default_preview.png')
    }
  },
  mounted() {
    this.pre = this.preview;
  },
  methods: {  }
}
</script>

<style scoped>
.container__video {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 0;
  gap: 19px;

  width: 33%;
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
  text-decoration: none;
  border-bottom: 0;
}
.username, .name, .username:hover, .name:hover, .name:active, .name:focus {
  color: var(--color-text);
  text-decoration: none;
}
</style>