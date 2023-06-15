<template>
    <div>
      <h1 class="cent">UrFUbe</h1>
      <h2 class="cent">Вход</h2>
      <input v-model="obj.email" class="inp cent" type="email" placeholder="Почта">
      <input v-model="obj.password" class="inp cent" type="password" placeholder="Пароль">
      <span style="color: var(--color-waiting)">{{error}}</span>
      <button @click="login" class="btn cent btn__submit" type="submit">Войти</button>
      <button @click="$router.push('/')" class="btn cent btn__exit" type="reset">Отмена</button>
    </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "LoginForm",

  methods: {
    ...mapActions([
        'login'
      ]),
    async login() {
      if (this.obj.email && this.obj.password) {
        let json = JSON.stringify(this.obj);
        await this.login(json)
            .catch((er) => {
              if (er.response && er.response.status === 400)
                this.error = "Неверный логин или пароль"})
      }
    }
  },
  data() {
    return {
      obj: {
        email: "",
        password: ""
      },
      error: ''
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