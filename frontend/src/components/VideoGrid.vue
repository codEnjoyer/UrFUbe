<template>
  <div class="container">
    <video-promo
        v-for="video in videos"
        :video="video"
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
  data() {
    return {
      videos: Array
    }
  },
  mounted() {
    //TODO: get videos
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