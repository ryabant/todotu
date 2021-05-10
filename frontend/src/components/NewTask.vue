<template>
  <div>
    <a class="button is-large is-link" @click="confirmAddTask">
      <span class="icon is-medium">
        <i class="fas fa-lg fa-plus"></i>
      </span>
    </a>
    <modal-add-task
      ref="modal_add_task"
      :tags="tags"
      @new-task="addTask"
    ></modal-add-task>
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
  props: { boardId: Number, tags: Object },
  data() {
    return {
      tasks: [],
      title: "",
      body: "",
      board: "",
      errors: [],
    };
  },
  methods: {
    addTask(item) {
      if (item.title) {
        axios({
          method: "post",
          url: "api/tasks/",
          data: {
            title: item.title,
            body: item.body,
            priority: item.priority,
            tags: item.tags,
            board: this.boardId,
          },
        })
          .then((response) => {
            let newTask = {
              id: response.data.id,
              title: item.title,
              body: item.body,
              priority: item.priority,
              tags: item.tags,
              board: this.boardId,
            };
            this.$emit("add-task", newTask);
            this.$refs.modal_add_task.show = false;
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              this.$refs.modal_add_task.errors = this.errors;
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");
              this.$refs.modal_add_task.errors = this.errors;
              console.log(JSON.stringify(error));
            }
          });
      }
    },
    confirmAddTask() {
      this.$refs.modal_add_task.show = true;
    },
  },
};
</script>