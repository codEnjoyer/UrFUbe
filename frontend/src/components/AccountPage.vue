<template>
  <div class="list">
    <div class="label_cont">
      <span v-if="is_load" style="width: 400px"><p>Загрузка</p></span>
      <h1>{{datas.user.username}}</h1>
    </div>
    <video-list :video_arr="datas.videos" />
  </div>
</template>

<script>
import VideoList from "@/components/VideoList.vue";
import {mapActions} from "vuex";

export default {
  name: "AccountPage",
  components: {VideoList},
  data() {
    return {
      datas: {
        videos: Array,
        user: {
          name: ''
        }
      },
      is_load: false
    }
  },
  async mounted() {
    let id = this.$route.params.user_id;
    if (!!id) {
      let f = { user_id: id}
      this.is_load = true;
      let r = await this.get_user({ user_id: id });
      if (r && r.status === 200) {
        this.datas.user = r.data.user
        this.datas.videos = r.data.videos
      } else {
        this.$router.push('/error')
      }
      this.is_load = false;
    } else {
      this.user = await this.account_me();
    }
    console.log(this.user)
  },
  methods: {
    ...mapActions([
        'account_me',
        'get_user'
      ]),
  }
}
</script>

<style scoped>
.list {
  width: 80%;
  align-self: center;
}
h1 {
  margin-left: 3%;
  font-size: 42px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>