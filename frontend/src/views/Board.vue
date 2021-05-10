<template>
  <div class="board">
    <div class="columns">
      <div class="column">
        <div class="container is-max-desktop">
          <Nav />
          <Menu
            :boardId="board.id"
            v-bind:tags="tags"
            :boardName="board.name"
            @update-tags="getTags"
          />

          <hr />
          <div
            class="is-flex is-flex-wrap-wrap is-justify-content-space-around is-align-content-stretch"
          >
            <NewTask
              :boardId="board.id"
              v-bind:tags="tags"
              @add-task="onAddTask"
            />
            <Tasks
              v-for="task in board.tasks"
              v-bind:task="task"
              v-bind:key="task.id"
              v-bind:tags="tags"
              @update-board="updateBoard"
            />
          </div>
          <hr />
          <Footer />
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
import Footer from "../components/Footer.vue";

export default {
  name: "Board",
  components: {
    Nav,
    Tasks,
    Menu,
    NewTask,
    Footer,
  },
  data() {
    return {
      board: {
        tasks: [],
      },
      tags: {},
    };
  },
  mounted() {
    this.getBoard();
    this.getTags();
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
    getTags() {
      axios({
        method: "get",
        url: `api/tags/`,
      })
        .then((response) => {
          this.tags = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>