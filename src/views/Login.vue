<template>
  <div class="register-form-container">
    <form class="register-form" @submit.prevent>
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
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

      <div class="mt-2">
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
      <button
        @click="handleOnSubmit"
        type="submit"
        class="btn btn-primary btn-block mt-3"
      >
        Login
      </button>
      <router-link to="/register">Register</router-link>
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
      this.signIn({ email: this.email, password: this.password }).then(
        (user) => {
          console.log("login/user", user);
          this.$router.push({ name: "Home" });
        }
      );
    },
  },
};
</script>

<style lang="scss"></style>
