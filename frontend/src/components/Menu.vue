<template>
  <div class="box">
    <nav class="level">
      <div class="level-left">
        <div class="level-item" v-for="board in boards" v-bind:key="board.id">
          <router-link :to="'/boards/' + board.id">
            <div class="tags">
              <span class="tag is-medium"
                >{{ board.name }}<button class="delete is-small"></button
              ></span>
            </div>
          </router-link>
        </div>
        <div class="level-item">
          <a href="#"><span class="tag is-link is-medium">+</span></a>
        </div>
      </div>
      <a>Completed &#127942;</a>
    </nav>
  </div>
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