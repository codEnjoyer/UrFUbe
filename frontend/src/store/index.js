import { createStore } from "vuex";

import videos from './modules/videos';
import users from './modules/users';

export default createStore({
  modules: {
    videos,
    users,
  }
});