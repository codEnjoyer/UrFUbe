<template>
  <div class="dialog">
    <div class="dialog__content">
      <RegistrationForm @register="register" @exit="exit" v-if="route_path === '/register'" />
      <LoginForm v-if="route_path === '/auth'" @login="login" @exit="exit"/>
      <UploadForm v-if="route_path === '/upload'" />
    </div>
  </div>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm.vue";
import LoginForm from "@/components/LoginForm.vue";
import UploadForm from "@/components/UploadForm.vue";

export default {
  components: {
    RegistrationForm,
    LoginForm,
    UploadForm
  },
  name: 'dialog-window',
  methods: {
    register(formData) {
      this.$router.push('/');
    },
    exit() {
      this.$router.go(-1);
    },
    login(formData) {
      this.$router.push('/');
    }
  },
  computed: {
    route_path() {
      return this.$route.path;
    }
  }
}
</script>

<style scoped>
.dialog {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
}

.dialog__content {
  margin: auto;
  background: var(--color-main);
  color: var(--color-text);
  border-radius: 12px;
  min-height: 50px;
  min-width: 300px;
  padding: 70px;
  text-align: center;
  display: flex;
}
</style>