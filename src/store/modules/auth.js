import firebase from "firebase";
import Vue from "vue";

const auth = {
  state: {
    currentUser: null,
  },
  getters: {
    currentUser(state) {
      return state.currentUser;
    },
  },

  actions: {
    createUser({ commit }, payload) {
      return firebase
        .auth()
        .createUserWithEmailAndPassword(payload.email, payload.password)
        .then((user) => {
          return firebase
            .firestore()
            .collection("users")
            .doc(user.user.uid)
            .set({
              firstName: payload.name,
              lastName: payload.lastName,
              email: payload.email,
              fullName: `${payload.name} ${payload.lastName}`,
              todos: [],
              inProgress: [],
              revision: [],
              check: [],
              done: [],
            })
            .then(function(docRef) {
              console.log("Document written with ID: ", docRef);
              commit("setCurrentUserHandler", user);
            })
            .catch(function(error) {
              console.error("Error adding document: ", error);
            });
        })
        .catch((err) => {
          console.log(err);
          var errorCode = err.code;
          var errorMessage = err.message;
          Vue.notify({
            group: "notification",
            title: "Error",
            text: err.message,
          });
        });
    },

    signIn({ commit }, payload) {
      return firebase
        .auth()
        .signInWithEmailAndPassword(payload.email, payload.password)
        .then((user) => {
          commit("setCurrentUserHandler", user.user);
        })
        .catch((err) => {
          Vue.notify({
            group: "notification",
            title: "Error",
            text: err.message,
          });
        });
    },
  },

  mutations: {
    setCurrentUserHandler(state, payload) {
      state.currentUser = payload;
    },
  },
};

export default auth;
