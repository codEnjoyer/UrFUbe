<template>
  <div class="list">
    <div class="label_cont">
      <h1>{{username}}</h1>
    </div>
    <video-list />
  </div>
</template>

<script>
import VideoList from "@/components/VideoList.vue";

export default {
  name: "AccountPage",
  components: {VideoList},
  data() {
    return {
      username: "sadasdasd asdasd  sada sd asd   sdad a sasdasd asdasdasd asdasdasdasdasd asdasd asdasd asdasdasd asda sd asd asdd"
    }
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