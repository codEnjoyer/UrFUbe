<template>
  <div class="container">
    <video-promo
        v-for="video in videos"
        :name="video.name"
        :video_id="video.id"
        :preview="video.preview"
        :user_id="video.user_id"
        :user_name="video.username"
        :watches="video.watches"
        :key="video.id"
    />
  </div>
</template>

<script>
import VideoPromo from "@/components/VideoPromo.vue";

export default {
  name: "VideoGrid",
  components: {
    VideoPromo
  },
  props: {
    videos: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.container{
  padding-top: 3%;
  border-bottom: black 2px;
  display: flex;
  flex-direction: row;
  gap: 4px;
  justify-content: space-around;
  width: 100%;
  height: 100%;
  flex-wrap: wrap;
}
</style>