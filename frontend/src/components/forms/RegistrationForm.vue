<template>
    <div>
      <h1 class="cent">UrFUbe</h1>
      <h2 class="cent">Регистрация</h2>
      <input v-model="username" class="inp cent" placeholder="Имя">
      <input v-model="email" class="inp cent" type="email" placeholder="Почта">
      <input v-model="password" class="inp cent" type="password" placeholder="Пароль">
      <input v-model="pass_password" class="inp cent" type="password" placeholder="Повторите пароль">
      <button @click="register" class="btn cent btn__submit" type="submit">Зарегистрироваться</button>
      <button @click="$emit('exit')" class="btn cent btn__exit" type="reset">Отмена</button>
    </div>
</template>

<script>

export default {
  name: "register",
  data() {
    return {
      email: String = '',
      username: String = '',
      password: String = '',
      pass_password: String = ''
    }
  },
  methods: {
    register() {
      if (this.email && this.password && this.username && this.password === this.pass_password) {
        const form = new FormData();
        form.set('email', this.email);
        form.set('user', this.email);
        form.set('password', this.email);
        this.$emit('register');
      }
    }
  },

}
</script>

<style scoped>
.inp {
  font-size: large;
  margin: 20px;
  display: flex;
  flex-direction: row;
  padding: 10px 20px;
  gap: 20px;
  width: 300px;
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
.waiting {
  background-color: var(--color-waiting);
}

.cent{
  margin-left: auto;
  margin-right: auto;
}

h1 {
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 700;
  font-size: 48px;
  line-height: 47px;
  margin-bottom: 30px;
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