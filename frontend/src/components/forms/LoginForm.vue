<template>
    <div>
      <h1 class="cent">UrFUbe</h1>
      <h2 class="cent">Вход</h2>
      <input v-model="email" class="inp cent" type="email" placeholder="Почта">
      <input v-model="password" class="inp cent" type="password" placeholder="Пароль">
      <button @click="login" class="btn cent btn__submit" type="submit">Войти</button>
      <button @click="$emit('exit')" class="btn cent btn__exit" type="reset">Отмена</button>
    </div>
</template>

<script>

export default {
  name: "register",

  methods: {
    login() {
      if (this.email && this.password) {
        const form = new FormData();
        form.set('email', this.email);
        form.set('password', this.password);
        this.$emit('login', form)
      }
    }
  },
  data() {
    return {
      email: String = "",
      password: String = ""
    }
  }

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
  width: 70%;
}

div {
  text-align: center;
  margin-right: auto;
  margin-left: auto;
}
</style>