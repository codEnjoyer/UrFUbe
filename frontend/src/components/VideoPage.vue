<template>
  <video :key="video.file">
    <source :src="video.file">
  </video>
  <div class="video__text">
      <div>
        <a class="name">
          <p>{{video.name}}</p>
        </a>
      </div>
       <div class="username">
         <p> Автор: {{video.username}} </p>
       </div>
     <p class="username">Просмотры: {{video.watches}}</p>
    </div>
</template>

<script>
export default {
  name: "VideoPage",
  data() {
    return {
      video: {

      }
    }
  },
  mounted() {
    // TODO: getVideo
    this.video.file = "https://drive.google.com/file/d/1sF52C2yzqb1ri7AamkmRZGpz4iyHy1UC/view?usp=sharing"
  }
}
</script>

<style scoped>

</style>