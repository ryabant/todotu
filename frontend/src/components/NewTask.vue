<template>
  <div>
    <a class="button is-light is-medium" @click="confirmAddTask">
      <span class="icon-text">
        <span class="icon is-medium">
          <i class="fas fa-lg fa-plus"></i>
        </span>
        <span class="title is-4">Add task</span>
      </span>
    </a>
    <modal-add-task ref="modal_add_task" @new-task="addTask"></modal-add-task>
  </div>
</template>

<script>
import axios from "axios";
import ModalAddTask from "../components/modal-add-task.vue";
export default {
  name: "NewTask",
  components: {
    ModalAddTask,
  },
  props: ["boardId"],
  data() {
    return {
      tasks: [],
      body: "",
      board: "",
    };
  },
  methods: {
    addTask(item) {
      if (item.body) {
        axios({
          method: "post",
          url: "api/tasks/",
          data: {
            body: item.body,
            board: this.boardId,
          },
        })
          .then((response) => {
            let newTask = {
              id: response.data.id,
              body: item.body,
              board: this.boardId,
            };
            this.$emit("add-task", newTask);
            this.$refs.modal_add_task.show = false;
            // this.body = "";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    confirmAddTask() {
      this.$refs.modal_add_task.show = true;
    },
  },
};
</script>