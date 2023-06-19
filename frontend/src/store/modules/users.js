import axios from 'axios';

const state = {
    is_auth: false,
    user: null
};

const getters = {
    is_authorised: state => state.is_auth,
    get_user: state => state.user
};

const actions = {
    get_video: async function ({getters}, params) {
        if (!getters.is_authorised) {
            return await axios.get(`video/${params.video_id}`, {params: params})
        } else {
            return await axios.get(`video/auth/${params.video_id}`, {params: params})
        }
    },
    check_authorise: async function({ commit, dispatch }){
        let r = await axios.get("protected")
        if (!!r && r.status === 200){
            let res = await dispatch("account_me")
            commit('set_auth', res)
        } else {
            commit('logout')
        }
    },
    registration: async function ({dispatch}, json) {
        let r = await axios.post('auth/register', json, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        if (!!r && r.status === 201) {
            let obj = {
                username: JSON.parse(json).email,
                password: JSON.parse(json).password
            }
            await dispatch('login', obj);
        }
        return r

    },
    login: async function ({dispatch}, obj) {
        let r = await axios.post('auth/login', obj, {
            headers: {
                'access': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }});
        if (r && r.status === 204) {
            dispatch('check_authorise');
        }
        return r;
    },
    async account_me() {
        let response = await axios.get(`user`);
        return response.data
    },
    async get_user({}, form) {
        return await axios.get(`user/${form.user_id}`)
    },
    async logOut({ commit }) {
        await axios.post('auth/logout');
        commit('logout');
    }
};

const mutations = {
    set_auth(state, data) {
        state.is_auth = true;
        state.user = data
    },
    logout(state) {
        state.is_auth = false;
        state.user = null
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};