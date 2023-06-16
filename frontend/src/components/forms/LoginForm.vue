<template>
    <div>
      <h1 class="cent">UrFUbe</h1>
      <h2 class="cent">Вход</h2>
      <span v-if="is_load" style="width: 400px"><p>Загрузка</p></span>
      <input v-model="obj.username" class="inp cent" type="email" placeholder="Почта">
      <input v-model="obj.password" class="inp cent" type="password" placeholder="Пароль">
      <span style="color: var(--color-waiting)">{{error}}</span>
      <button @click="auth" class="btn cent btn__submit" type="submit">Войти</button>
      <button @click="$router.push('/')" class="btn cent btn__exit" type="reset">Отмена</button>
      <p>Нет аккаунта? <router-link to="/register">Регистрация</router-link></p>
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
    async auth() {
      if (!this.is_load)
        if (this.obj.username && this.obj.password) {
          let form = new FormData();
          form.append('username', this.username)
          form.append('password', this.password)
          this.is_load = true;
          let r = await this.login(form)
          this.is_load = false;
          if (r && r.status === 400)
                  this.error = "Неверный логин или пароль"
          else if (r && r.status === 200) {
             this.$router.push('/');
           } else {
             this.error = 'Повторите попытку'
           }
        } else {
          this.error = 'Заполните все поля'
        }
    }
  },
  data() {
    return {
      obj: {
        username: "",
        password: ""
      },
      error: '',
      is_load: ''
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