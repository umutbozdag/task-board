import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    currentUserData: null,
  },
  getters: {
    currentUserData(state) {
      return state.currentUserData;
    },
  },
  mutations: {
    setCurrentUserDataHandler(state, payload) {
      state.currentUserData = payload;
    },
  },
  actions: {},
  modules: {
    auth,
  },
});
