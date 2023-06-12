<template>
  <div class="container">
    <h1>Тут будет видео.</h1>
    <video-promo></video-promo>
  </div>
</template>

<script>
import VideoPromo from "@/components/VideoPromo.vue";

export default {
  name: "VideoGrid",
  components: {
    VideoPromo
  }
}
</script>

<style scoped>
container{
  border-bottom: black 2px;
}
</style>