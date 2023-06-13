<template>
  <div class="list">
    <h1 class="label">Видео по запросу: "{{$route.params.req}}"</h1>
    <div class="container">
      <video-promo-horizontal
          v-for="video in videos"
          :video="video"
          :key="video.id"
      />
      <video-promo-horizontal />
    </div>
  </div>
</template>

<script>
import VideoPromoHorizontal from "@/components/VideoPromoHorizontal.vue";

export default {
  name: "VideoList",
  components: {
    VideoPromoHorizontal
  },
  data() {
    return {
      videos: Array
    }
  },
  props: {
    video_arr: { type: Array, required: true },

  }
}
</script>

<style scoped>
.container{
  padding-top: 3%;
  border-bottom: black 2px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  justify-content: space-around;
  width: 100%;
  height: 100%;
}
.label {
  font-family: 'Roboto';
  font-weight: 700;
  font-size: 32px;
  line-height: 39px;
  /* identical to box height */

  display: flex;
  align-items: center;

  /* black */

  color: var(--color-text);
}
.list {
  width: 80%;
  align-self: center;
}
</style>