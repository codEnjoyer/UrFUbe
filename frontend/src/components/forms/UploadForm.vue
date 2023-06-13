<template>
<h1>Загрузка видео</h1>
  <div>
    <input type="file" accept="video/mp4, video/mov">
    <input type="file" accept="image/jpeg, image/png">
  </div>
  <input type="text" placeholder="Название видео">
  <div>
    <button>Отмена</button>
    <button>Опубликовать</button>
  </div>
</template>

<script>
export default {
  name: "UploadForm"
}
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 32px;
}
</style>