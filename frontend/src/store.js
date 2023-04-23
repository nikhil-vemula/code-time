import { createStore } from "vuex";
import router from "./router";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000";
// axios.defaults.baseURL = "https://code-time-backend.onrender.com";

const store = createStore({
  state() {
    return {
      isLoggedIn: false,
      loginFailed: false,
      user: null,
      question: {},
      reviseQuestions: [],
      problemsCount: '',
      solvedProblemsCount: ''
    };
  },
  mutations: {
    setLoggedIn(state, payload) {
      state.isLoggedIn = payload;
    },
    setUser(state, payload) {
      state.user = payload;
      if (localStorage) {
        if (payload)
          localStorage.setItem('user', JSON.stringify(state.user))
        else
          localStorage.removeItem('user')
      }
    },
    setLoginFailed(state, payload) {
      state.loginFailed = payload;
    },
    setQuestions(state, payload) {
      state.questions = payload;
    },
    setQuestion(state, payload) {
      state.question = payload
    },
    setReviseQuestions(state, payload) {
      state.reviseQuestions = payload
    },
    setProblemsCount(state, payload) {
      state.problemsCount = payload
    },
    setSolvedProblemsCount(state, payload) {
      state.solvedProblemsCount = payload
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
      commit("setUser", null);
      commit("setLoggedIn", false);
      router.push("/");
    },
    createUser({ commit }, userDetails) {
      axios
        .post("/createuser", {
          firstname: userDetails.first_name,
          lastname: userDetails.last_name,
          email: userDetails.email,
          password: userDetails.password,
        })
        .then(function (response) {
          let data = response.data;
          console.log(response)
          if (response.status != 200) {
            return;
          }
          commit('setUser', data[0])
          commit('setLoggedIn', true)
          router.push('/')
        })
        .catch(function (error) {
          console.log(error);
        });
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
    markQuestion({state, commit}, parms) {
      axios
        .get("/marksolved/" + parms.question_id + '/' + parms.solved)
        .then(function (response) {
          console.log("Marked!")
          alert("Successfully marked the question")
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    fetchReviseQuestions({state, commit}) {
      axios
        .get("/questionsrevise/" + state.user.user_id)
        .then(function (response) {
          commit('setReviseQuestions', [...response.data])
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    fetchProblemsCount({state, commit}) {
      axios
        .get("/get_problems_count/" + state.user.user_id)
        .then(function (response) {
          commit('setProblemsCount', response.data.count)
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    fetchSolvedProblemsCount({state, commit}) {
      axios
        .get("/get_solved_problems_count/" + state.user.user_id)
        .then(function (response) {
          commit('setSolvedProblemsCount', response.data.count)
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deleteQuestion({state,  commit}, parms) {
      console.log(parms)
      axios.delete('/question/' + parms['question_id']).then((response) => {
        console.log(response)
      })
    }
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
    getReviseQuestions(state) {
      return state.reviseQuestions;
    },
    getProblemsCount(state) {
      return state.problemsCount;
    },
    getSolvedProblemsCount(state) {
      return state.solvedProblemsCount;
    },
  },
});

export default store;
