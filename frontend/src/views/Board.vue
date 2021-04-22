<template>
  <div class="board">
    <Nav />
    <div class="columns">
      <div class="column">
        <Boards />
      </div>
      <div class="column">
        <NewTask />
        <Tasks
          v-for="task in completedTasks"
          v-bind:key="task.id"
          v-bind:task="task"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Nav from "../components/Nav.vue";
import Tasks from "../components/Tasks.vue";
import Boards from "../components/Boards.vue";
import NewTask from "../components/NewTask.vue";

export default {
  name: "Board",
  components: {
    Nav,
    Tasks,
    Boards,
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
  updated() {
    this.getBoard();
  },
  computed: {
    completedTasks() {
      return this.board.tasks.filter((task) => {
        return !task.completed;
      });
    },
  },
  methods: {
    async getBoard() {
      const id = this.$route.params.id;
      await axios({
        method: "get",
        url: `api/boards/${id}`,
      })
        .then((response) => {
          this.board = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>