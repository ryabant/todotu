<template>
  <div class="cards">
    <div class="card" v-for="board in boards" v-bind:key="board.id">
      <div class="card-content">
        <div class="columns">
          <div class="column is-four-fifths">
            {{ board.name }}
          </div>
          <button class="button" @click="goToBoard(board.id)">
            <i class="fas fa-check"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Boards",
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