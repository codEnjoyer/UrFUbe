import axios from 'axios';

const state = {
  user: null
};

const getters = {
  is_authorised: state => !!state.user,
  user: state => state.user,
};

const actions = {
  registration: async function ({dispatch}, json) {
    return await axios.post('auth/register', json, {
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(async (r) => {
      if (!!r && r.status === 200) {
        let form = new FormData();
        form.append('username', json.email)
        form.append('password', json.password)
        await dispatch('login', form);
      }
    })
  },
  login: async function ({commit}, form) {
    let r = await axios.post('auth/login', form, {
    }).then((response) => {
      if (!!response && response.status === 200)
          commit('set_auth', response.data.user);
        }
    );
    return r;
  },
  upload: async function (form) {
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