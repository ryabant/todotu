<template>
  <div class="login">
    <div class="columns">
      <div class="column is-4 is-offset">
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

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-dark">Login</button>
            </div>
          </div>
          <hr />
          Or <router-link to="/users/register">click here</router-link> to sign
          up!
        </form>
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
            this.$store.commit("setToken", token, this.username);
            axios.defaults.headers.common["Authorization"] = "Token " + token;
            localStorage.setItem("token", token);
            localStorage.setItem("username", this.username);
            this.$router.push("/boards/1");
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