<template>
  <div class="board">
    <div class="columns">
      <div class="column">
        <div class="container is-max-desktop">
          <Nav />
          <Menu :boardId="board.id" />

          <hr />
          <div
            class="is-flex is-flex-wrap-wrap is-justify-content-space-around is-align-content-stretch"
          >
            <NewTask :boardId="board.id" @add-task="onAddTask" />
            <Tasks
              v-for="task in board.tasks"
              v-bind:task="task"
              v-bind:key="task.id"
              @update-board="updateBoard"
            />
          </div>
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

export default {
  name: "Board",
  components: {
    Nav,
    Tasks,
    Menu,
    NewTask,
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