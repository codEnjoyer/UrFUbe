import axios from 'axios';

const state = {
  user: null
};

const getters = {
  is_authorised: state => !!state.user,
  user: state => state.user,
};

const actions = {
  async registration({dispatch}, json) {
    await axios.post('auth/register', json, {
          headers: {
            'Content-Type': 'application/json'
          }
      }).catch((error) => {
          if (error.status === 400)
            return 'Пароль должен быть более 8 символов'
        }).then(async (r) => {
          console.log(json);
          await dispatch('login', json);
        })
  },
  async login({commit}, json) {
    let response_object = {
      username: json.email,
      password: json.password
    }
    await axios.post('auth/login', JSON.stringify(response_object), {
          headers: {
            'Content-Type': 'application/json'
          }
      }).then((response) => {
              commit('set_auth', response.data.user);
            }
        );
  },
  async upload(form) {
    await axios.post(`video/upload`, form);
  },
  async account_me({state}) {
    let {data} = await axios.get(`user/${state.user.id}`);
    return data;
  },
  async get_user({}, user_id) {
    console.log(user_id)
    return await axios.get(`user/${user_id}`)
  },
  async logOut({commit}) {
    await axios.post('auth/logout');
    commit('logout');
  }
};

const mutations = {
  set_auth(state, user) {
    state.user = user;
  },
  logout({state}){
    state.user = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};