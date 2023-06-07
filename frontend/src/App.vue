<template>
  <div>
  <Header @page="change_page" @search="search" @theme="change_theme" :is-authorised="true"/>
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
      current_page: 'home',
      theme: ''
    }
  },
  methods: {
    change_page(page) {
      this.current_page = page
    },
    search(request) {
      this.change_page('search')
      alert(request)
    },
    change_theme() {
      this.theme = this.theme === 'darkMode' ? 'lightMode' : 'darkMode';
      document.documentElement.setAttribute('data-theme', this.theme);
      localStorage.setItem('theme', this.theme);
    },
    getMediaPreference() {
      const hasDarkPreference = window.matchMedia(
      "(prefers-color-scheme: dark)").matches;
      if (hasDarkPreference)
        return 'darkMode';
      else {
        return 'lightMode';
      }
    }
  },
  mounted() {
    let localTheme = localStorage.getItem('theme');
    const theme = localStorage.getItem('theme') || this.getMediaPreference();
    document.documentElement.setAttribute('data-theme', theme);
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

:root {
  --color-main: #E5E5E5;
  --color-element: #FFFFFF;
  --color-text: #303030;
  --invert-light: invert(0%);
}
[data-theme="darkMode"] {
  --color-main: #303030;
  --color-element: #404040;
  --color-text: #E5E5E5;
  --invert-light: invert(100%);
}

body {
  font-family: Roboto;
  color: var(--color-text);
  background: var(--color-main);
}
.icon-light {
  filter: var(--invert-light);
}
</style>