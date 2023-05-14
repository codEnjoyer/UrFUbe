<template>
  <Header></Header>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm.vue";
import Header from "@/components/Header.vue";
export default {
  components: {
    RegistrationForm,
    Header,
  },
  name: "App",
  data() {
    return {
      likes: 0,
    }
  },
  methods: {
    addLike() {
      this.likes += 1;
    }
  }
}
</script>

<style scoped>

</style>