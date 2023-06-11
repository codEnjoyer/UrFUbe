<template>
    <div>
      <h1 class="cent">UrFUbe</h1>
      <h2 class="cent">Регистрация</h2>
      <input class="inp cent" placeholder="Логин">
      <input class="inp cent" type="password" placeholder="Пароль">
      <input class="inp cent" type="password" placeholder="Повтори пароль">
      <button @click="register" class="btn cent btn__submit" type="submit">Зарегистрироваться</button>
      <button @click="$router.go(-1)" class="btn cent btn__exit" type="reset">Отмена</button>
    </div>
</template>

<script>

export default {
  name: "register",

  methods: {
    register() {
      this.$router.push('/')
    }
  }

}
</script>

<style scoped>
.inp {
  font-size: large;
  width: 100%;
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
.btn {
  border-width: 0;
  width: 80%;
  margin-bottom: 15px;
  border-radius: 10px;
}
.btn__exit, .btn__exit:active {
  background: var(--color-element);
  color: var(--color-text);
  width: 50%;
}
.btn__submit, .btn__submit:active {
  background-color: #B2FFC8;
  color: #404040;
}

div {
  text-align: center;
  margin-right: auto;
  margin-left: auto;
}
</style>