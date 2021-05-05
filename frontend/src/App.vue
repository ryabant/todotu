<template>
  <router-view />
</template>

<script>
import axios from "axios";
export default {
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>
