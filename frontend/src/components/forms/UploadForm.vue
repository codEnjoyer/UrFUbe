<template>
  <div class="container">
    <h1>Загрузка видео</h1>
    <div class="input-file-row input-file">
      <div class="file__container">
        <input @change="check" ref="video" type="file" accept="video/mp4, video/ogg, video/mkv, video/webm">
        <span>{{object.video_file.name}}</span>
      </div>
      <div class="file__container pre">
        <input @change="check" ref="preview" type="file" accept="image/jpeg, image/png">
        <span>{{object.preview_file.name}}</span>
      </div>
    </div>
    <span style="color: var(--color-waiting)">{{error}}</span>
    <div class="input-file-column">
      <input v-model="object.name" class="inp" type="text" placeholder="Название видео">
      <textarea v-model="object.description" class="inp" type="text" placeholder="Описание" />
    </div>
    <div class="input-file-row">
      <button @click="$router.go(-1)" class="btn cent btn__exit">Отмена</button>
      <button @click="upload_video" class="btn cent btn__submit">Опубликовать</button>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";
import axios from "axios";
export default {
  name: "UploadForm",
  data() {
    return {
      object: {
        preview_file: Image,
        video_file: File,
        name: '',
        description: '',
      },
      error: ''
    }
  },
  methods: {
    async upload_video() {
      if (this.object.video_file && this.object.name) {
        //let form = new FormData();
        // form.append('name', this.object.name)
        // form.append('description', this.object.description)
        // form.append('video_file', byteArray)
        // form.append('preview_file', byteArray_1)
        let obj = JSON.stringify({
          name: this.object.name,
          description: this.object.description
        })
        console.log(obj)
        const responce = await axios.post("video/upload", obj, this.object.video_file, this.object.preview_file, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
        });
        this.upload({}, { obj: obj, video_file: this.object.video_file, preview_file: this.object.preview_file })
      } else {
        this.error = 'Загрузите видео и укажите его название'
      }
    },
    ...mapActions([
        'upload'
      ]),
    check() {
      let video = this.$refs.video.files[0];
      let preview = this.$refs.preview.files[0];
      if (video)
        this.object.video_file = video
      if (preview)
        this.object.preview_file = preview
    }
  }
}
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 32px;
}
.container {
  width: 45%;
  align-self: center;
  margin-left: auto;
  margin-right: auto;
}
.container > * {
  padding: 30px 20px;
}
.input-file-row {
	display: flex;
  flex-direction: row;
}
.input-file-row button {
  width: 40%;
}
.file__container span {
  width: 100%;
  overflow: hidden;
}
.file__container {
  width: 344px;
  height: 200px;
  background: center url("../../assets/upload_background.png");
  border-radius: 10px;
  margin-right: 10px;
  margin-left: 10px;
}
.pre {
  background: center url("../../assets/preview_background.png");
}
.file__container input {
  margin-top: auto;
  margin-bottom: auto;
  width: 100%;
  height: 100%;
  opacity: 0;
}
.file__container span {
  position	: relative;
  z-index: 10;
  text-align: center;
}
.input-file-column {
  display: flex;
  flex-direction: column;
}
.cent{
  margin-left: auto;
  margin-right: auto;
}
.btn {
  border-width: 0;
  width: 30px;
  margin-bottom: 15px;
  border-radius: 10px;
}
.btn__exit, .btn__exit:active {
  background: var(--color-waiting);
  color: #404040;
}
.btn__submit, .btn__submit:active {
  background-color: var(--color-succses);
  color: #404040;
}
.inp {
  font-size: large;
  margin: 20px;
  display: flex;
  flex-direction: row;
  padding: 10px 20px;
  gap: 20px;
  width: 300px;
  height: 39px;
  outline:none;
  overflow: hidden;

  background: var(--color-element);
  color: var(--color-text);
  border-radius: 10px;
  border-width: 0;

  flex: none;
  order: 0;
  flex-grow: 0;
}
</style>