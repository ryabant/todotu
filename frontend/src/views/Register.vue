<template>
  <div class="register">
    <div class="container">
      <div class="section is-medium">
        <div class="column is-half is-offset-one-quarter">
          <div class="box">
            <div>
              <a href="/"><img alt="logo" src="../assets/logo.png" /></a>
            </div>
            <hr />
            <h1 class="title">Sign up</h1>
            <form @submit.prevent="submitForm">
              <div class="field">
                <label>Username</label>
                <div class="control">
                  <input type="text" class="input" v-model="username" />
                </div>
              </div>

              <div class="field">
                <label>Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password" />
                </div>
              </div>

              <div class="field">
                <label>Repeat password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password2" />
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-link">Sign up</button>
                </div>
              </div>
              <hr />
              Already signed up?
              <router-link to="/users/login">Login!</router-link>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }
      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };
        axios
          .post("users/register/", formData)
          .then(() => {
            this.$router.push("/users/login");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");
              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>