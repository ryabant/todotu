<template>
  <a class="box">
    <div class="card-content">
      <p class="title">
        {{ task.title }}
      </p>
    </div>
  </a>
</template>

<script>
import axios from "axios";

export default {
  name: "Tasks",
  props: {
    task: Object,
  },
  components: {},
  methods: {
    setStatus(task_id) {
      axios({
        method: "patch",
        url: "api/tasks/" + task_id + "/",
        data: {
          completed: true,
        },
      }).then(() => {
        this.$emit("update-board");
      });
    },
    deleteTask(task_id) {
      axios({
        method: "delete",
        url: "api/tasks/" + task_id + "/",
      }).then(() => {
        this.$emit("update-board");
      });
    },
    confirmDelete() {
      this.$refs.modal.show = true;
    },
  },
};
</script>