<template>
  <div class="board">
    <div class="columns">
      <div class="column">
        <div class="container is-max-desktop">
          <Nav />
          <Menu v-bind:tags="tags" @update-tags="getTags" />

          <hr />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Nav from "../components/Nav.vue";
import Menu from "../components/Menu.vue";

export default {
  name: "AddBoard",
  components: {
    Nav,
    Menu,
  },
  data() {
    return {
      tags: {},
    };
  },
  mounted() {
    this.getTags();
  },
  methods: {
    getTags() {
      axios({
        method: "get",
        url: `api/tags/`,
      })
        .then((response) => {
          this.tags = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>