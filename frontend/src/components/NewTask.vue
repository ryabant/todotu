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
          <button class="button is-link">Add Task</button>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "NewTask",
  props: ["boardId"],
  data() {
    return {
      tasks: [],
      body: "",
      board: "",
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
            board: this.boardId,
          },
        })
          .then((response) => {
            let newTask = {
              id: response.data.id,
              body: this.body,
              board: this.boardId,
            };
            this.tasks.unshift(newTask);
            this.body = "";
            this.board = "";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>