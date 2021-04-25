<template>
  <aside class="menu has-background-light">
    <ul class="menu-list">
      <li><router-link to="/" exact>Inbox</router-link></li>
      <li><router-link to="/about" exact>About</router-link></li>

      <li>
        <a>Boards</a>
        <ul v-for="board in boards" v-bind:key="board.id">
          <router-link tag="li" :to="'/boards/' + board.id">
            {{ board.name }}
          </router-link>
        </ul>
      </li>

      <li><a>Completed</a></li>
    </ul>
  </aside>
</template>

<script>
import axios from "axios";

export default {
  name: "Menu",
  data() {
    return {
      boards: [],
    };
  },
  props: {
    board: Object,
  },
  mounted() {
    this.getBoards();
  },
  methods: {
    async getBoards() {
      await axios({
        method: "get",
        url: "api/boards/",
      })
        .then((response) => {
          this.boards = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>