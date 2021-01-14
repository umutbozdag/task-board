<template>
  <div class="register-form-container">
    <form class="register-form" @submit.prevent="handleOnSubmit">
      <div class="row mb-2">
        <div class="col-lg-6">
          <div class="form-group">
            <label for="exampleInputEmail1">First name</label>
            <input
              type="text"
              class="form-control"
              v-model="name"
              placeholder="First name"
            />
          </div>
        </div>
        <div class="col-lg-6">
          <div class="form-group">
            <label for="exampleInputEmail1">Last name</label>
            <input
              type="text"
              class="form-control"
              v-model="lastName"
              placeholder="Last name"
            />
          </div>
        </div>
      </div>
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

        <div class="form-group">
          <label for="exampleInputPassword2">Password (again)</label>
          <input
            type="password"
            class="form-control"
            v-model="passwordAgain"
            id="exampleInputPassword2"
          />
        </div>
      </div>
      <!-- <div class="form-group form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1" />
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div> -->
      <button type="submit" class="btn btn-primary btn-block mt-3">
        Submit
      </button>
      <router-link to="/login">Login</router-link>
    </form>
  </div>
</template>

<script>
import firebase from "firebase";
import { mapActions } from "vuex";

export default {
  name: "Register",
  data() {
    return {
      email: null,
      password: null,
      passwordAgain: null,
      name: null,
      lastName: null,
    };
  },
  methods: {
    ...mapActions(["createUser"]),
    handleOnSubmit() {
      if (this.password === this.passwordAgain) {
        this.createUser({
          email: this.email,
          password: this.password,
          name: this.name,
          lastName: this.lastName,
        }).then((response) => {
          this.$router.push({ name: "Home" });
          console.log("response", response);
        });
      }
    },
  },
};
</script>

<style lang="scss">
.register-form {
  width: 500px;
}

.register-form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
