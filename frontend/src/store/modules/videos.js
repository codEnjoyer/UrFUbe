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
  upload: async function ({}, obj) {
    let query = obj.query;
    obj.form.forEach(el => console.log(el));
    let response = await axios.post(`video/upload`,
        obj.form,
        {params: query, headers: {'Content-Type': 'multipart/form-data'}});
    return response;
  },
  remove_video: async function({}, video_id) {
    await axios.delete(`video/remove/${video_id}`, {params: {video_id: video_id}})
  },
  add_comment: async function ({}, params) {
    let data = {
            text: params.text
          };
    await axios.post(`video/${params.video_id}/comment`, {}, {params: data});
  },
  add_reaction: async function ({}, params) {
    let data = {
            reaction_type: params.reaction_type
          };
    await axios.post(`video/${params.video_id}/reaction`, {}, {params: params});
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