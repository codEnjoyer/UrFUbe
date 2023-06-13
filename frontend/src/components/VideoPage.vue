<template>
  <video>
    <source>
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
  }
}
</script>

<style scoped>

</style>