<template>
  <div class="box">
    <div class="field is-grouped is-grouped-multiline">
      <div class="control" v-for="board in boards" v-bind:key="board.id">
        <!-- <span class="tag is-medium">Completed &#127942;</span> -->
        <div class="tags has-addons">
          <router-link class="tag is-medium" :to="'/boards/' + board.id">
            {{ board.name }}
            <!-- <button class="delete is-small" @click="deleteBoard(board.id)"></button> -->
            <!-- <modal-delete
                  ref="modal"
                  @confirm="deleteBoard(board.id)"
                ></modal-delete> -->
          </router-link>
          <a class="tag is-delete is-medium" @click="deleteBoard(board.id)"></a>
        </div>
      </div>
      <div class="control">
        <a
          ><span class="tag is-link is-medium" @click="confirmAddBoard"
            >+</span
          ></a
        >

        <modal-add-board ref="modal" @add-board="addBoard"></modal-add-board>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import ModalDelete from "../components/modal-delete.vue";
import ModalAddBoard from "../components/modal-add-board.vue";
export default {
  name: "Menu",
  components: {
    // ModalDelete,
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
    deleteBoard(board_id) {
      console.log(board_id);
      axios({
        method: "delete",
        url: "api/boards/" + board_id + "/",
      }).then(() => {
        this.getBoards();
        this.$router.push("1");
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
          })
          .then(() => {
            this.getBoards();
            this.$refs.modal.show = false;
          })
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