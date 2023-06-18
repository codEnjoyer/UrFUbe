<template>
  <div>
  <Header @theme="change_theme"/>
  <router-view></router-view>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import router from "@/router/router";

export default {
  components: {
    Header
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
  --background-color: #D9D9D9;
  --color-waiting: #FFB2B2;
  --color-success: #B2FFC8;
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