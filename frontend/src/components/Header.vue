<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">UrFUbe</router-link>
        <div class="collapse navbar-collapse">
          <form class="d-flex search-input" role="search">
            <input key="search_input" placeholder="Поиск" v-model="search_request" @submit="search" aria-label="Search">
            <a class="btn" @click="search">
              <img class="icon-light" src="../assets/header/loupe.png">
            </a>
          </form>
          <router-link to="/upload" class="nav-link nav-item" aria-current="page" v-if="$store.getters.is_authorised">
            <img class="icon-light" src="../assets/header/upload.png">
          </router-link>
          <div class="nav-item dropdown">
            <a data-bs-toggle="dropdown" aria-expanded="false">
              <img class="icon-light" src="../assets/header/account.png">
            </a>
            <ul class="dropdown-menu" v-if="!$store.getters.is_authorised">
              <li>
                <router-link to="/register" class="dropdown-item btn">Регистрация</router-link>
              </li>
              <li>
                <router-link to="/auth" class="dropdown-item btn">Вход</router-link>
              </li>
            </ul>
            <ul class="dropdown-menu" v-else>
              <li>
                <router-link to="/account/me" class="dropdown-item btn">Аккаунт</router-link>
              </li>
              <li>
                <button @click="logout" class="dropdown-item btn">Выйти</button>
              </li>
            </ul>
          </div>
          <a @click="change_theme" class="nav-link nav-item theme-button" aria-current="page"></a>
        </div>
      </div>
    </nav>
    <hr>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      search_request: "",
      main_theme: true,
      is_authorised: false
    }
  },
  methods: {
    search() {
      if (this.search_request !== '') {
        this.$router.push('/search/' + this.search_request)
        //TODO: search
        this.search_request = '';
      }
    },
    change_theme() {
      this.$emit('theme')
    },
    async logout() {
      await this.$store.actions.logOut();
    }
  }
}
</script>

<style scoped>
.btn:active {
  border: var(--color-element);
}
.btn{
  border-radius: 0;
}

.dropdown-menu {
  transform: translateX(-50%);
  left: 50%;
  top: 120%;
  align-items: flex-start;
  gap: 10px;
  padding: 30%;


  background: var(--color-element);
  border-radius: 10px;
}

.dropdown-item:hover{
  background-color: var(--color-element);
}

.dropdown {
  margin-right: 2%;
}
.dropdown-item{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 10px;

  width: 100%;
  height: 100%;

  border-bottom: 1px solid var(--color-text);
  color: var(--color-text);
  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}
.nav-link{
  margin-right: 2%;
}
.navbar-brand {
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  line-height: 47px;
  /* identical to box height */

  display: flex;
  align-items: center;

  /* black */

  color: var(--color-text);
}

input {
  border: var(--color-element);
  width: 150%;
  height: 150%;
  outline:none;
  background-color: var(--color-element);
  color: var(--color-text)
}

form {
  max-width: 1000px;
  width: 700px;
  height: 40px;
  margin: 10px auto;
}
hr{
  margin: 0;
}
.search-input{
  flex-direction: row;
  align-items: center;
  padding: 10px 20px;
  gap: 20px;

  width: 467px;
  left: calc(50% - 467px/2 - 136.5px);
  top: 25%;
  bottom: 25%;
  border: var(--color-element);

  /* white */

  background: var(--color-element);
  border-radius: 10px;
}
.theme-button {
  border-radius: 50%;
  width: 30px;
  height: 30px;
  background-color: var(--color-text);
}
</style>