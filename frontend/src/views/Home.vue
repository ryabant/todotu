<template>
  <div class="home">
    <div class="container">
      <div class="section is-medium">
        <div class="column is-half is-offset-one-quarter">
          <div class="box">
            <div class="is-flex is-justify-content-center">
              <img alt="logo" src="../assets/logo.png" />
            </div>
            <hr />
            <div class="is-flex is-justify-content-space-evenly">
              <router-link
                to="/users/login"
                class="button is-link is-outlined is-medium"
                >Login</router-link
              >
              <router-link
                to="/users/register"
                class="button is-outlined is-medium"
                >Register</router-link
              >
            </div>
          </div>
          <div class="content has-text-centered">
            <p>
              The source code
              <a href="https://github.com/ryabant/todotu">link</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>