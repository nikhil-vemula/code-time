import { createStore } from "vuex";
import router from "./router";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:5000";

const store = createStore({
  state() {
    return {
      isLoggedIn: true,
      loginFailed: false,
      user: {
        user_id: 1,
      },
      question: {}
    };
  },
  mutations: {
    setLoggedIn(state, payload) {
      state.isLoggedIn = payload;
    },
    setUser(state, payload) {
      state.user = payload;
    },
    setLoginFailed(state, payload) {
      state.loginFailed = payload;
    },
    setQuestions(state, payload) {
      state.questions = payload;
    },
    setQuestion(state, payload) {
      state.question = payload
    }
  },
  actions: {
    userLogin({ commit }, { email, password }) {
      axios
        .post("/users", {
          username: email,
          password: password,
        })
        .then(function (response) {
          let data = response.data;
          if (data && data.length > 0) {
            commit("setLoginFailed", false);
            commit("setLoggedIn", true);
            commit("setUser", data[0]);
            router.push("/");
          } else {
            commit("setLoginFailed", true);
            commit("setLoggedIn", false);
            commit("setUser", null);
            router.push("/signin");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    userSignOut({ commit }) {
      commit("setLoggedIn", false);
      router.push("/");
    },
    getQuestionsForUser({ state, commit }) {
      axios
        .post("/questions", {
          user_id: state.user.user_id,
        })
        .then(function (response) {
          let data = response.data;
          commit("setQuestions", data);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    saveQuestion({ state, commit }, question) {
      question.user_id = state.user.user_id;
      if ('question_id' in question) {
        let question_id = question.question_id
        axios
        .put("/question/" + question_id, {...question})
        .then(function (response) {
          console.log("Saved successfully")
        })
        .catch(function (error) {
          console.log(error);
        });
      } else {
        axios
        .post("/question", {...question})
        .then(function (response) {
          let question_id = response.data.question_id
          router.push("/question/" + question_id)
        })
        .catch(function (error) {
          console.log(error);
        });
      }
      
    },
    getQuestion({commit}, question_id) {
      axios
        .get("/question/" + question_id,)
        .then(function (response) {
          let question = response.data[0]
          commit('setQuestion', question)
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  getters: {
    isLoggedIn(state) {
      return state.isLoggedIn;
    },
    isLoginFailed(state) {
      return state.loginFailed;
    },
    getQuestions(state) {
      return state.questions;
    },
    getQuestion(state) {
      return state.question;
    },
  },
});

export default store;
