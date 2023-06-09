<template>
  <div>
  <Header @page="change_page" @search="search" @theme="change_theme" :is-authorised="true"/>
  <router-view></router-view>
  <dialog-window v-if="current_page === 'register' || current_page === 'auth' || current_page === 'upload'">
    <RegistrationForm @exit="change_page('')" />
  </dialog-window>
  </div>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm.vue";
import Header from "@/components/Header.vue";
import VideoGrid from "@/components/VideoGrid.vue";
import DialogWindow from "@/components/DialogWindow.vue";
import router from "@/router/router";

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
      current_page: '',
      theme: '',
      is_authorised: false
    }
  },
  methods: {
    change_page(page) {
      this.current_page = page;
      this.router().push('/' + page);
    },
    router() {
      return router;
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
    },
    logout() {
      this.is_authorised = false;
      this.current_page = ''
    },
    addHashToLocation(params) {
      this.$router.push('/' + params);
      history.pushState(
        {},
        null,
         this.$router.path
      )
    }
  },
  mounted() {
    let localTheme = localStorage.getItem('theme');
    const theme = localTheme || this.getMediaPreference();
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