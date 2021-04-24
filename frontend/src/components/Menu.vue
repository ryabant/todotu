<template>
  <aside class="menu has-background-light">
    <ul class="menu-list">
      <li><a>Inbox</a></li>
      <li><a>Today</a></li>
    </ul>
    <ul class="menu-list">
      <li>
        <a class="is-active">Boards</a>
        <ul v-for="board in boards" v-bind:key="board.id">
          <li>
            <a @click="goToBoard(board.id)">{{ board.name }}</a>
          </li>
        </ul>
      </li>
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
        .then((error) => {
          console.log(error);
        });
    },
    goToBoard(board_id) {
      this.$router.push(`/boards/${board_id}/`);
    },
  },
};
</script>