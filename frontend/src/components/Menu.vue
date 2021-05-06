<template>
  <div class="box">
    <div class="field is-grouped is-grouped-multiline">
      <div v-for="board in boards" v-bind:key="board.id">
        <router-link class="navbar-item" :to="'/boards/' + board.id">
          {{ board.name }}
        </router-link>
      </div>
      <p class="control">
        <a class="button is-link" @click="confirmAddBoard">+</a>

        <modal-add-board ref="modal" @add-board="addBoard"></modal-add-board>
      </p>
    </div>
  </div>
</template>




<script>
import axios from "axios";
import ModalAddBoard from "../components/modal-add-board.vue";
export default {
  name: "Menu",
  components: {
    ModalAddBoard,
  },
  data() {
    return {
      boards: [],
      name: "",
    };
  },
  props: {
    board: Object,
  },
  mounted() {
    this.getBoards();
  },
  watch: {
    $route() {
      this.getBoards();
    },
  },
  methods: {
    getBoards() {
      axios({
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
    confirmDelete() {
      this.$refs.modal.show = true;
    },
    addBoard(item) {
      if (item.name) {
        axios({
          method: "post",
          url: "api/boards/",
          data: {
            name: item.name,
          },
        })
          .then((response) => {
            let newBoard = {
              id: response.data.id,
              name: item.name,
            };
            this.boards.push(newBoard);
            this.$router.push(`/boards/${newBoard.id}`);
            this.getBoards();
            this.$refs.modal.show = false;
          })
          .then(() => {})
          .catch((error) => {
            console.log(error);
          });
      }
    },
    confirmAddBoard() {
      this.$refs.modal.show = true;
    },
  },
};
</script>
