import { createStore } from "vuex";
import router from "./router";

const store = createStore({
  state() {
    return {
      isLoggedIn: false,
    };
  },
  mutations: {
    setLoggedIn(state, payload) {
      state.isLoggedIn = payload
    }
  },
  actions: {
    userLogin ({ commit }, {email, password}) {
      commit('setLoggedIn', true)
      router.push('/')
    },
    userSignOut ({ commit}) {
      commit('setLoggedIn', false)
      router.push('/')
    },
  },
  getters: {
    isLoggedIn(state) {
      return state.isLoggedIn
    },
  },
});

export default store;
