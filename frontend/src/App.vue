<template>
  <div>
  <Header @page="change_page" @search="search" :last_page="current_page" :is-authorised="true"/>
  <VideoGrid v-if="current_page === 'home'" />
  <dialog-window v-if="current_page === 'register' || current_page === 'auth' || current_page === 'upload'">
    <RegistrationForm @exit="change_page('home')" />
  </dialog-window>
  </div>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm.vue";
import Header from "@/components/Header.vue";
import VideoGrid from "@/components/VideoGrid.vue";
import DialogWindow from "@/components/DialogWindow.vue";
export default {
  components: {
    DialogWindow,
    RegistrationForm,
    Header,
    VideoGrid
  },
  name: "App",
  data() {
    return {
      current_page: 'home'
    }
  },
  methods: {
    change_page(page) {
      this.current_page = page
    },
    search(request) {
      this.change_page('search')
      alert(request)
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

body {
  font-family: Roboto;
  color: #303030;
  background: #E5E5E5;
}

</style>