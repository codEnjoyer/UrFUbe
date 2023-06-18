<template>
  <div class="video__promo">
    <router-link :to="'/video/' + video.video_id" class="preview">
      <img :src="pre" >
    </router-link>
    <div class="video__text">
      <router-link :to="'/video/' + video.video_id" style="text-decoration: none; color: inherit;">
        <a class="name">
          <p>{{video.name}}</p>
        </a>
       </router-link>
       <router-link :to="'/account/' + video.user_id" class="username">
         <p> Автор: {{video.username}} </p>
       </router-link>
     <p class="username">Просмотры: {{video.count_views}}</p>
    </div>
    <div class="buttons" v-if="$route.path === '/account/me'">
      <button class="btn cent btn__submit" @click="delete_video">Удалить</button>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";
export default {
  name: "VideoPromoHorizontal",
  props: {
    video: { type: Object, required: true }
  },
  data() {
    return {
      pre: require('../assets/video/default_preview.jpeg'),
    }
  },
  methods: {
    ...mapActions([
        'remove_video'
      ]),
    async delete_video(){
      await this.remove_video(this.video.video_id)
      this.$emit("remove_item", this.video.video_id)
    }
  },
  mounted() {
    if (this.video.preview_url) {
      this.pre = this.video.preview_url;
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
.buttons {
  margin-left: auto;
  right: 0;
}

.preview img {
  width: 172px;
  height: 100px;
  object-fit: cover;
  margin: 20px 30px;
  overflow: hidden;
  background-color: var(--color-element);
  border-radius: 10px;
}
.video__text {
  margin-top: auto;
  margin-bottom: auto;
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

.btn {
  border-width: 0;
  width: 200px;
  margin-bottom: 15px;
  margin-top: 45px;
  border-radius: 10px;
}
.btn__submit, .btn__submit:active {
  background-color: #B2FFC8;
  color: #404040;
}
</style>