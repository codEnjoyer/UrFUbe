import axios from 'axios';

const state = {
  user: null
};

const getters = {
  is_authorised: state => !!state.user,
  user: state => state.user,
};

const actions = {
  get_video: async function ({getters}, params) {
    if (!getters.is_authorised) {
      return await axios.get(`video/${params.video_id}`, {params: params})
    } else {
      return await axios.get(`auth/video/${params.video_id}`, {params: params})
    }
  },
  registration: async function ({dispatch}, json) {
    return await axios.post('auth/register', json, {
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(async (r) => {
      console.log(json);
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
      console.log(form);
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
  async get_user({}, form) {
    console.log(form)
    return await axios.get(`user/${form.user_id}`, form)
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