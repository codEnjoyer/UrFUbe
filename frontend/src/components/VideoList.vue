<template>
  <div class="list__video">
    <h1 class="label" v-if="$route.params.req">Видео по запросу: "{{$route.params.req}}"</h1>
    <div class="container" v-if="videos!==null">
      <video-promo-horizontal
          v-for="video in videos"
          :video="video"
          :key="video.video_id"
      />
    </div>
  </div>
</template>

<script>
import VideoPromoHorizontal from "@/components/VideoPromoHorizontal.vue";
import {mapActions} from "vuex";

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
    video_arr: { type: Array }
  },
  mounted() {
    if (this.video_arr) {
      this.videos = this.video_arr;
    } else if (this.$route.params.req) {
      let req = this.$route.params.req
      console.log(req)
      let r = this.search_video({ name: req })
      if (r && r.status === 200) {
        this.video_arr = r.data;
      } else {
      this.$router.push('/error')
      }
    }
  }, methods: {
    ...mapActions([
        'search_video'
      ]),
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
.list__video {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}
</style>