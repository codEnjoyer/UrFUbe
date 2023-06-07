<template>
  <div>
    <h1>UrFUbe</h1>
    <h1>Регистрация</h1>
    <input class="inp" placeholder="Логин">
    <input class="inp" placeholder="Пароль">
    <button class="btn" @click="exit">Отмена</button>
  </div>
</template>

<script>

export default {
  name: "RegistrationForm",

  methods: {
    exit() {
      this.$emit('exit')
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