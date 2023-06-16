import axios from 'axios';

const actions = {
  async search_video({}, req) {
    let l = await axios.get(`video/search`, {params: req})
    console.log(l)
    return l
  },
  get_comments: async function ({}, params) {
    return await axios.get(`video/${params.video_id}/comments`)
  },
  get_homepage: async function () {
    return await axios.get('/');
  },
  get_videos: async function ({}, params) {
    return await axios.get(`video/user/${params.user_id}`, { params: params })
  },
  upload: async function (form) {
    await axios.post(`video/upload`, form, {headers: {'Content-Type': 'multipart/form-data', 'accept': 'application/json'}});
  },
  add_comment: async function ({}, params) {
    await axios.post(`video/${params.video_id}/comment`, { params: params })
  },
  add_reaction: async function ({}, params) {
    await axios.post(`video/${params.video_id}/comment`, { params: params })
  },
};
const state = {}
const getters = {}
const mutations ={}
export default {
  state,
  getters,
  actions,
  mutations
};