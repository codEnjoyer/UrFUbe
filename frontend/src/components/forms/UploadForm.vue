<template>
  <div class="container">
    <h1>Загрузка видео</h1>

        <div class="input-file-row input-file">
            <div class="file__container">
                <input @change="check" ref="video" type="file" accept="video/mp4, video/ogg, video/mkv, video/webm">
                <p v-if="!!object.video_file">{{ object.video_file.name }}</p>
            </div>
            <div class="file__container pre">
                <input @change="check" ref="preview" type="file" accept="image/jpeg, image/png">
                <p v-if="!!object.preview_file">{{ object.preview_file.name }}</p>
            </div>
        </div>
        <p>Максимальный размер загружаемых файлов - 512 Мб</p>
      <div class="container d-flex justify-content-center" v-if="is_uploading">
          <div class="spinner-border" role="status">
              <span class="sr-only">Loading...</span>
          </div>
      </div>
        <span style="color: var(--color-waiting)">{{ error }}</span>
        <div class="input-file-column">
            <input v-model="object.name" class="inp" type="text" placeholder="Название видео">
            <textarea v-model="object.description" class="inp" type="text" placeholder="Описание"/>
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
        preview_file: null,
        video_file: null,
        name: '',
        description: '',
      },
      error: '',
      is_uploading: false,
    }
  },
  methods: {
    async upload_video() {
        this.object.name = this.object.name.trim();
      if (this.object.video_file && this.object.name && this.object.name.length < 40) {
          this.is_uploading = true;
          let form = new FormData();
          form.append('video_file', this.object.video_file);
          if(this.object.preview_file){
            form.append('preview_file', this.object.preview_file);
          }
          let response = (await this.upload({
              form: form,
              query: {
                      name: this.object.name,
                      description: this.object.description
              }
          })).response;
          console.log(response)
          if (response && response.status === 400){
            this.error = response.data.detail
          }
          else if (response && response.status === 200){
              this.$router.push("/")
          }
      } else if (this.object.name.length > 40){
        this.error = 'Слишком большое название видео'
      } else {
        this.error = 'Загрузите видео и укажите его название'
      }
      this.is_uploading = false;
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
.file__container p {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-decoration: none;
  overflow-wrap: anywhere;
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
  background-color: var(--color-success);
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