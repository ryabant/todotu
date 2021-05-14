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
  name: "Inbox",
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
    this.getInbox();
  },
  watch: {
    $route() {
      this.getInbox();
    },
  },
  methods: {
    getInbox() {
      axios({
        method: "get",
        url: `api/tasks/inbox/`,
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
      this.getInbox();
    },
  },
};
</script>