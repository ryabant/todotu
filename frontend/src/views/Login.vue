<template>
  <div class="login">
    <div class="container">
      <div class="section is-medium">
        <div class="column is-half is-offset-one-quarter">
          <div class="box">
            <div>
              <a href="/tasks/inbox"
                ><img alt="logo" src="../assets/logo.png"
              /></a>
            </div>
            <hr />
            <h1 class="title">Log in</h1>
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

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-link">Login</button>
                </div>
              </div>
              <hr />
              Don't have an account?
              <router-link to="/users/register">Sign up!</router-link>
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
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      this.errors = [];
      if (this.username === "") {
        this.errors.push("The username is missing");
      }
      if (this.password === "") {
        this.errors.push("The password is too short");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };
        await axios
          .post("users/login/", formData)
          .then((response) => {
            const token = response.data.token;
            this.$store.commit("setToken", token);
            axios.defaults.headers.common["Authorization"] = "Token " + token;
            localStorage.setItem("token", token);
            this.$router.push("/tasks/inbox");
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