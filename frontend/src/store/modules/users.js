import axios from 'axios';

const state = {
    is_auth: false
};

const getters = {
    is_authorised: state => state.is_auth
};

const actions = {
    get_video: async function ({getters}, params) {
        if (!getters.is_authorised) {
            return await axios.get(`video/${params.video_id}`, {params: params})
        } else {
            return await axios.get(`video/auth/${params.video_id}`, {params: params})
        }
    },
    check_authorise: async function({ commit }){
        console.log("check_authorize")
        let r = await axios.get("protected")
        console.log(r)
        if (!!r && r.status === 200){
            console.log("set_auth")
            commit('set_auth')
        } else {
            console.log("logout")
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
            console.log(obj);
            await dispatch('login', obj);
        }
        return r

    },
    login: async function ({commit}, obj) {
        console.log()
        let r = await axios.post('auth/login', obj, {
            headers: {
                'access': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }});
        console.log(r)
        if (r && r.status === 204) {
            commit('set_auth');
        }
        return r;
    },
    async account_me() {
        let {data} = await axios.get(`user`);
        return data;
    },
    async get_user({}, form) {
        console.log(form)
        return await axios.get(`user/${form.user_id}}`, form)
    },
    async logOut({ commit }) {
        await axios.post('auth/logout');
        commit('logout');
    }
};

const mutations = {
    set_auth(state) {
        state.is_auth = true;
    },
    logout(state) {
        state.is_auth = false;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};