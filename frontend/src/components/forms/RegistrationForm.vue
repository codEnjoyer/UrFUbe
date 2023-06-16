<template>
    <div>
      <h1 class="cent">UrFUbe</h1>
      <h2 class="cent">Регистрация</h2>
        <div>
          <span v-if="is_load" style="width: 400px"><p>Загрузка</p></span>
          <input v-model="object.username" class="inp cent" placeholder="Имя">
          <input v-model="object.email" class="inp cent" type="email" placeholder="Почта">
          <input v-model="object.password" class="inp cent" type="password" placeholder="Пароль">
          <input v-model="pass_password" class="inp cent" type="password" placeholder="Повторите пароль">
          <span style="color: var(--color-waiting)">{{error}}</span>
          <button class="btn cent btn__submit" @click="register">Зарегистрироваться</button>
        </div>
      <button @click="$router.push('/')" class="btn cent btn__exit">Отмена</button>
      <p>Есть аккаунт? <router-link to="/auth">Вход</router-link></p>
    </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "RegistrationForm",
  data() {
    return {
      object: {
        email:  '',
        password:  '',
        username: ''
      },
      error: '',
      pass_password:  '',
      is_load: false
    }
  },
  methods: {
     ...mapActions([
        'registration'
      ]),
    async register() {
       if (!this.is_load) {
         if(this.object.password.length < 8) {
           this.error = "Пароль должен содержать более 8 символов"
         } else if (this.object.email && this.object.password && this.object.username && this.object.password === this.pass_password) {
           let obj = JSON.stringify(this.object);
           this.is_load = true
           let re = await this.registration(obj);
           this.$router.push('/');
           // if (re && re.status === 200) {
           // } else {
           //   this.error = 'Повторите попытку'
           // }
           this.is_load = false
         } else if (this.object.password !== this.pass_password) {
           this.error = 'Пароль не совпадает'
         } else {
           this.error = 'Пожалуйста, заполните все поля'
         }
       }
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