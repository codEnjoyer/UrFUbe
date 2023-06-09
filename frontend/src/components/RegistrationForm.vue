<template>
    <div>
      <h1 class="cent">UrFUbe</h1>
      <h2 class="cent">Регистрация</h2>
      <input class="inp cent" placeholder="Логин">
      <input class="inp cent" placeholder="Пароль">
      <button class="btn cent" @click="exit">Отмена</button>
    </div>
</template>

<script>
import router from "@/router/router";

export default {
  name: "RegistrationForm",

  methods: {
    router() {
      return router
    },
    exit() {
      this.$emit('exit')
      this.router().go(-1)
    }
  }

}
</script>

<style scoped>
.inp {
  font-size: large;
  width: 80%;
  margin: 20px;
  display: flex;
  flex-direction: row;
  padding: 10px 20px;
  gap: 20px;
  height: 39px;
  outline:none;

  background: var(--color-element);
  color: var(--color-text);
  border-radius: 10px;
  border-width: 0;

  flex: none;
  order: 0;
  flex-grow: 0;
}

.dw {
  width: 100%;
  height: 100%;
}

.cent{
  margin-left: auto;
  margin-right: auto;
}

h1 {
  width: 126px;
  height: 47px;

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  line-height: 47px;
}
.btn, .btn:active, .btn:hover {
  width: 50%;
  background-color: #B2FFC8;
  border-width: 0;
  color: #404040;
}
div {
  text-align: center;
  margin-right: auto;
  margin-left: auto;
}
</style>