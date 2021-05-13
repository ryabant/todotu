<template>
  <div class="box">
    <div class="field is-grouped is-grouped-multiline">
      <div class="control">
        <a class="button"><i class="fas fa-star"></i></a>
      </div>
      <div class="control">
        <a class="button"><i class="fas fa-inbox"></i></a>
      </div>
      <div class="control" v-for="board in boards" v-bind:key="board.id">
        <div class="tags are-large">
          <router-link class="navbar-item tag" :to="'/boards/' + board.id">
            {{ board.name }}
          </router-link>
        </div>
      </div>
      <p class="control">
        <a class="button is-link" @click="confirmAddBoard"
          ><i class="fas fa-plus"></i
        ></a>

        <modal-add-board
          ref="modal_add_board"
          @add-board="addBoard"
        ></modal-add-board>
      </p>
      <p class="control">
        <a class="button is-danger" @click="confirmDeleteBoard"
          ><i class="fas fa-trash"></i
        ></a>

        <modal-delete
          ref="modal_del_board"
          @confirm="deleteBoard(boardId)"
          v-bind:boardName="boardName"
        ></modal-delete>
      </p>
      <div class="navbar-end">
        <a class="button is-warning" @click="onGetTags"
          ><i class="fas fa-tags"></i
        ></a>
      </div>
      <modal-tags
        ref="modal_tags"
        @update-tags="updateTags"
        v-bind:tags="tags"
        v-bind:boardId="boardId"
      ></modal-tags>
    </div>
  </div>
</template>




<script>
import axios from "axios";
import ModalAddBoard from "../components/modal-add-board.vue";
import ModalDelete from "../components/modal-delete.vue";
import ModalTags from "../components/modal-tags.vue";

export default {
  name: "Menu",
  components: {
    ModalAddBoard,
    ModalDelete,
    ModalTags,
  },
  data() {
    return {
      boards: [],
      name: "",
      index: "",
    };
  },
  props: ["boardId", "boardName", "tags"],
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
            this.$refs.modal_add_board.show = false;
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    confirmAddBoard() {
      this.$refs.modal_add_board.show = true;
    },
    deleteBoard(boardId) {
      axios({
        method: "delete",
        url: "api/boards/" + boardId + "/",
      }).then(() => {
        this.$router.push("/boards/");
        this.$refs.modal_del_board.show = false;
      });
    },
    confirmDeleteBoard() {
      this.$refs.modal_del_board.show = true;
    },
    onGetTags() {
      this.$refs.modal_tags.show = true;
    },
    updateTags() {
      this.$emit("update-tags");
    },
  },
};
</script>
