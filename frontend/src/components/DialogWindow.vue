<template>
  <div class="dialog">
    <div class="dialog__content">
      <RegistrationForm ref="el" @register="register" @exit="exit" v-if="route_path === '/register'" />
      <LoginForm ref="el" v-if="route_path === '/auth'" @login="login" @exit="exit"/>
    </div>
  </div>
</template>

<script>
import RegistrationForm from "@/components/forms/RegistrationForm.vue";
import LoginForm from "@/components/forms/LoginForm.vue";

export default {
  components: {
    RegistrationForm,
    LoginForm
  },
  name: 'dialog-window',
  methods: {
    async register(formData) {
      this.$router.push('/');
      await this.$nextTick();
      this.route_path = this.$route.path;
    },
    async exit() {
      this.$router.go(-1);
      await this.$nextTick();
      this.route_path = this.$route.path;
    },
    async login(formData) {
      this.$router.push('/');
      await this.$nextTick();
      this.route_path = this.$route.path;
    },
    OnRouteChange(route) {
      this.route_path = this.$route.path;
    }
  },
  data() {
    return {
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