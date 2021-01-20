<template>
  <div class="register-form-container">
    <form class="register-form" @submit.prevent>
      <div class="form-group">
        <label for="exampleInputEmail1" class="mt-5">Email address</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          v-model="email"
          placeholder="Enter email"
        />
        <small id="emailHelp" class="form-text text-muted"
          >We'll never share your email with anyone else.</small
        >
      </div>
      
      <div class="mt-4">
        <div class="form-group">
          <label for="exampleInputPassword1">Password</label>
          <input
            type="password"
            class="form-control"
            v-model="password"
            id="exampleInputPassword1"
          />
        </div>
      </div>
      <div class="loginBtns mt-4">
        <button
          @click="handleOnSubmit"
          type="submit"
          id="login-btn"
          class="btn btn-primary btn-block mt-3 btn-lg"
        >
          Login
          <i class="fas fa-sign-in-alt"></i>
        </button>
        <router-link to="/register" id="register-btn">Register</router-link>
     </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      email: null,
      password: null,
    };
  },
  methods: {
    ...mapActions(["signIn"]),
    handleOnSubmit() {
      if (this.email && this.password) {
        this.signIn({ email: this.email, password: this.password }).then(
          (user) => {
            console.log("login/user", user);
            this.$router.push({ name: "Home" });
          }
        );
      } else {
        this.$notify({
          group: "notification",
          title: "Error",
          type: "error",
          text: "Fill all the empty fields",
        });
      }
    },
  },
};
</script>

<style lang="scss"></style>
