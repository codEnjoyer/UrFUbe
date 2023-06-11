<template>
 <div class="container__video">
   <div class="preview__wrap">
     <img :src="pre" class="preview">
   </div>
 </div>
</template>

<script>
export default {
  name: "video-promo",
  props: {
    preview: { default: 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png' }
  },
  data() {
    return {
      pre: require('../assets/video/default_preview.png')
    }
  },
  mounted() {
    this.pre = this.preview;
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
</style>