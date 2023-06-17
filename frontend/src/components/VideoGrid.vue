<template>
  <div class="container" v-if="!is_load">
    <video-promo
        v-for="video in videos"
        :video="video"
        :key="video.video_id"
    />
  </div>
</template>

<script>
import VideoPromo from "@/components/VideoPromo.vue";
import {mapActions} from "vuex";

export default {
  name: "VideoGrid",
  components: {
    VideoPromo
  },
  data() {
    return {
        is_load: false,
      videos: Array
    }
  },
  methods: {
    ...mapActions([
        'get_homepage'
      ])
  },
  async mounted() {
      this.is_load = true;
    let r = await this.get_homepage()
    if (r && r.status === 200) {
      this.videos = r.data
    }
    else {
      this.$router.push('/error')
    }
    this.is_load = false;
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