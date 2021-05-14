<template>
  <div class="board">
    <div class="columns">
      <div class="column">
        <div class="container">
          <Nav />
          <Menu />

          <hr />
          <div
            class="is-flex is-flex-wrap-wrap is-justify-content-space-around is-align-content-stretch"
          >
            <NewTask @add-task="onAddTask" v-bind:tags="tags" />
            <Tasks
              v-for="task in tasks"
              v-bind:task="task"
              v-bind:key="task.id"
              @update-board="updateTasks"
              v-bind:tags="tags"
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
  name: "Important",
  components: {
    Nav,
    Tasks,
    Menu,
    NewTask,
    Footer,
  },
  data() {
    return {
      tasks: [],
      tags: [],
    };
  },
  mounted() {
    this.getTasks();
    this.getTags();
  },
  watch: {
    $route() {
      this.getTasks();
    },
  },
  methods: {
    getTasks() {
      axios({
        method: "get",
        url: `api/tasks/important/`,
      })
        .then((response) => {
          this.tasks = response.data;
        })
        .catch((error) => console.log(error));
    },
    onAddTask(item) {
      this.tasks.unshift(item);
    },
    updateTasks() {
      this.getTasks();
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