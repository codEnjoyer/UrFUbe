<template>
  <div class="dialog">
    <div class="dialog__content">
      <RegistrationForm v-if="$route.path === '/register'" />
      <LoginForm v-if="$route.path === '/auth'" />
    </div>
  </div>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm.vue";
import LoginForm from "@/components/LoginForm.vue";
export default {
  components: {
    RegistrationForm,
    LoginForm
  },
  name: 'dialog-window'
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