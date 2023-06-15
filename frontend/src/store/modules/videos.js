import axios from 'axios';
import header from "@/components/Header.vue";

const actions = {
  async get_video({}, video_id) {
    let {data} = await axios.get(`video/${video_id.video_id}`, { headers: { "Access-Control-Allow-Origin": `*`}})

    return data;
  },
  async search_video(req) {
    let videos = await axios.get(`video/search`, req)
    return videos;
  },
  async get_comments(id) {
    let comments = await axios.get(`video/${id}/comments`)
    return comments
  },
  async get_homepage() {
    let videos = await axios.get('/');
    return videos;
  },
  async upload(form) {
    await axios.post(`video/upload`, form);
  },
  async add_comment(video_id, text) {
    await axios.post(`video/${video_id}/comment`, { video_id: video_id, text: text })
  },
  async add_reaction(video_id, reaction_type) {
    await axios.post(`video/${video_id}/comment`, { video_id: video_id, reaction_type: reaction_type })
  }
};

export default {
  actions,
};