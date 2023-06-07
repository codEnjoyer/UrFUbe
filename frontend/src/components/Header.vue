<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" @click="go_to_page('home')">UrFUbe</a>
        <div class="collapse navbar-collapse">
          <form class="d-flex search-input" role="search">
            <input type="search" placeholder="Поиск" v-model="search_request" aria-label="Search">
            <button type="button" class="btn" @click="search">
              <img src="../assets/header/loupe.png">
            </button>
          </form>
          <a class="nav-link nav-item" aria-current="page" v-if="isAuthorised" @click="go_to_page('upload')">
            <img src="../assets/header/upload.png">
          </a>
          <div class="nav-item dropdown">
            <a data-bs-toggle="dropdown" aria-expanded="false">
              <img src="../assets/header/account.png">
            </a>
            <ul class="dropdown-menu" v-if="!isAuthorised">
              <li>
                <button class="dropdown-item btn" @click="go_to_page('register')">Регистрация</button>
              </li>
              <li>
                <button class="dropdown-item btn" @click="go_to_page('auth')">Вход</button>
              </li>
            </ul>
            <ul class="dropdown-menu" v-else>
              <li>
                <button class="dropdown-item btn" @click="go_to_page('account')">Аккаунт</button>
              </li>
              <li>
                <button class="dropdown-item btn" @click="go_to_page('exit')">Выйти</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
    <hr>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: {
    isAuthorised: {
      type: Boolean,
      default: false
    },
    last_page: {
      type: String
    }
  }, data() {
    return {
      search_request: '',
      current_page: 'home'
    }
  },
  methods: {
    search() {
      if (this.search_request !== '') {
        this.$emit('search', this.search_request)
        this.search_request = ''
        this.current_page = 'search'
      }
    },
    go_to_page(req) {
      if (this.current_page !== req) {
        this.$emit('page', req)
        this.current_page = req
        if (['register', 'auth', 'upload'].includes(this.current_page))
          this.current_page = 'home'
      }
    },
  }
}
</script>

<style scoped>

.btn:active {
  border: #FFFFFF;
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


  background: #FFFFFF;
  border-radius: 10px;
}

.dropdown-item:hover{
  background-color: #FFFFFF;
}

.dropdown {
  margin-right: 5%;
}
.dropdown-item{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 10px;

  width: 100%;
  height: 100%;

  /* grey */

  border-bottom: 1px solid #B0B0B0;

  /* Inside auto layout */

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

  color: #303030;
}

input {
  border: #FFFFFF;
  width: 150%;
  height: 150%;
  outline:none;
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
  border: #FFFFFF;

  /* white */

  background: #FFFFFF;
  border-radius: 10px;
}


</style>