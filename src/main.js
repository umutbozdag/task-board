import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import db from "@/database";
import firebase from "firebase";
import VModal from "vue-js-modal";
import Notifications from "vue-notification";

Vue.config.productionTip = false;

Vue.use(VModal);
Vue.use(Notifications);

firebase.auth().onAuthStateChanged(async (user) => {
  console.log(user);
  new Vue({
    router,
    store,
    created() {
      if (!user) {
        this.$router.push({ name: "Login" });
        // store.commit("setIsAuthenticatedHandler", false);
      } else {
        // store.commit("setIsAuthenticatedHandler", true);

        let docRef = db.collection("users").doc(user.uid);

        docRef
          .get()
          .then(function(doc) {
            if (doc.exists) {
              console.log("Document data:", doc.data());
              store.commit("setCurrentUserDataHandler", doc.data());
            } else {
              // doc.data() will be undefined in this case
              console.log("No such document!");
            }
          })
          .catch(function(error) {
            console.log("Error getting document:", error);
          });

        store.commit("setCurrentUserHandler", user);
      }
    },
    render: (h) => h(App),
  }).$mount("#app");
});
