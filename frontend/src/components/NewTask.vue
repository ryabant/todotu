<template>
  <div class="new-card">
    <form class="box" v-on:submit.prevent="addTask">
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
</template>

<script>
import axios from "axios";
export default {
  name: "NewTask",
  data() {
    return {
      tasks: [],
      body: "",
    };
  },
  methods: {
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
  },
};
</script>