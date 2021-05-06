<template>
  <div class="board">
    <div class="columns">
      <div class="column">
        <div class="container is-max-desktop">
          <Nav />
          <Menu />
          <div class="container">
            <div class="level">
              <div class="level-left">
                <div class="level-item">
                  <a class="button is-success is-small is-light"
                    >Completed &#11088;</a
                  >
                </div>
              </div>
              <div class="level-right">
                <div class="level-item">
                  <a
                    class="button is-danger is-small is-light"
                    @click="confirmDeleteBoard"
                    >Delete board</a
                  >
                </div>
              </div>
            </div>
            <modal-delete
              ref="modal"
              @confirm="deleteBoard(board.id)"
            ></modal-delete>
          </div>
          <NewTask :boardId="board.id" @add-task="onAddTask" />
          <Tasks
            v-for="task in completedTasks"
            v-bind:task="task"
            v-bind:key="task.id"
            @update-board="updateBoard"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Nav from "../components/Nav.vue";
import Tasks from "../components/Tasks.vue";
import Menu from "../components/Menu.vue";
import NewTask from "../components/NewTask.vue";
import ModalDelete from "../components/modal-delete.vue";

export default {
  name: "Board",
  components: {
    Nav,
    Tasks,
    Menu,
    NewTask,
    ModalDelete,
  },
  data() {
    return {
      board: {
        tasks: [],
      },
    };
  },
  mounted() {
    this.getBoard();
  },
  computed: {
    completedTasks() {
      return this.board.tasks.filter((task) => {
        return !task.completed;
      });
    },
  },
  watch: {
    $route() {
      this.getBoard();
    },
  },
  methods: {
    getBoard() {
      const id = this.$route.params.id;
      axios({
        method: "get",
        url: `api/boards/${id}`,
      })
        .then((response) => {
          this.board = response.data;
        })
        .then(() => {
          this.board;
        })
        .catch((error) => console.log(error));
    },
    onAddTask(item) {
      this.board.tasks.unshift(item);
    },
    updateBoard() {
      this.getBoard();
    },
    deleteBoard(board_id) {
      axios({
        method: "delete",
        url: "api/boards/" + board_id + "/",
      }).then(() => {
        this.$refs.modal.show = false;
        this.$router.push("/boards/"); // TODO
      });
    },
    confirmDeleteBoard() {
      this.$refs.modal.show = true;
    },
  },
};
</script>