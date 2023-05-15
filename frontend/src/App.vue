<template>
  <Header />
  <VideoGrid />
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm.vue";
import Header from "@/components/Header.vue";
import VideoGrid from "@/components/VideoGrid.vue";
export default {
  components: {
    RegistrationForm,
    Header,
    VideoGrid
  },
  name: "App",
  data() {
    return {  }
  },
  methods: {  }
}
</script>

<style scoped>

</style>