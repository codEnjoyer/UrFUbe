<template>
  <div class="list">
    <div class="label_cont">
      <h1>{{user.name}}</h1>
    </div>
    <video-list :video_arr="user.videos" />
  </div>
</template>

<script>
import VideoList from "@/components/VideoList.vue";
import {mapActions} from "vuex";
import users from "@/store/modules/users";

export default {
  name: "AccountPage",
  components: {VideoList},
  data() {
    return {
      user: {
        videos: Array,
        user: {
          name: ''
        }
      }
    }
  },
  async mounted() {
    let id = this.$route.params.user_id;
    if (!!id) {
      this.user = await this.get_user(id);
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