<template>
  <div class="home">
    <div class="columns">
      <Menu />

      <div class="column">
        <div class="cards">
          <div class="card">
            <div class="card-content">
              <form v-on:submit.prevent="addTask">
                <div class="field">
                  <div class="control">
                    <input
                      class="input"
                      type="text"
                      placeholder="Text input"
                      v-model="body"
                    />
                  </div>
                </div>
                <div class="field">
                  <p class="control">
                    <button class="button is-success">Add Task</button>
                  </p>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="cards">
          <div class="card" v-for="task in completedTasks" v-bind:key="task.id">
            <div class="card-content">
              <div class="columns">
                <div class="column">
                  <button class="button" @click="setStatus(task.id)">
                    <i class="fas fa-check"></i>
                  </button>
                </div>
                <div class="column is-four-fifths">
                  {{ task.body }}
                </div>

                <div class="column">
                  <button class="button is-danger" @click="confirmDelete">
                    <i class="fas fa-trash-alt"></i>
                  </button>

                  <modal-window
                    ref="modal"
                    @confirm="deleteTask(task.id)"
                  ></modal-window>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ModalWindow from "../components/modal-window.vue";
import Menu from "../components/Menu.vue";

export default {
  name: "Home",
  data() {
    return {
      tasks: [],
      body: "",
    };
  },
  components: {
    ModalWindow,
    Menu,
  },
  mounted() {
    this.getTasks();
  },
  computed: {
    completedTasks() {
      return this.tasks.filter((task) => {
        return !task.completed;
      });
    },
  },
  methods: {
    async getTasks() {
      await axios({
        method: "get",
        url: "api/tasks/",
      })
        .then((response) => {
          this.tasks = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async addTask() {
      if (this.body) {
        await axios({
          method: "post",
          url: "api/tasks/",
          data: {
            body: this.body,
            board: 1,
          },
        })
          .then((response) => {
            let newTask = {
              id: response.data.id,
              body: this.body,
            };
            this.tasks.unshift(newTask);

            this.body = "";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    async setStatus(task_id) {
      await axios({
        method: "patch",
        url: "api/tasks/" + task_id + "/",
        data: {
          completed: true,
        },
      });
      this.getTasks();
    },
    async deleteTask(task_id) {
      await axios({
        method: "delete",
        url: "api/tasks/" + task_id + "/",
      });
      this.getTasks();
    },
    confirmDelete() {
      this.$refs.modal.show = true;
    },
  },
};
</script>