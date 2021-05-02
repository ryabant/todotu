<template>
  <div class="level-item">
    <a href="#"
      ><span class="tag is-link is-medium" @click="confirmAddBoard">+</span></a
    >
    <modal-add-board ref="modal" @add-board="addBoard"></modal-add-board>
  </div>
</template>

<script>
import axios from "axios";
import ModalAddBoard from "../components/modal-add-board.vue";
export default {
  name: "NewBoard",
  components: {
    ModalAddBoard,
  },
  data() {
    return {
      boards: [],
      name: "",
    };
  },
  methods: {
    addBoard(item) {
      if (item.name) {
        axios({
          method: "post",
          url: "api/boards/",
          data: {
            name: item.name,
            owner: 1,
          },
        })
          .then((response) => {
            let newBoard = {
              id: response.data.id,
              name: item.name,
              owner: 1,
            };
            this.boards.push(newBoard);
            item.name = "";
          })
          .then(() => {})
          .catch((error) => {
            console.log(error);
          });
      }
      this.$refs.modal.show = false;
    },
    confirmAddBoard() {
      this.$refs.modal.show = true;
    },
  },
};
</script>