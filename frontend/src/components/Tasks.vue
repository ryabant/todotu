<template>
  <div class="tasks">
    <div class="box">
      <article class="media">
        <div class="media-left">
          <label class="checkbox">
            <input type="checkbox" @click="setStatus(task.id)" />
          </label>
        </div>
        <div class="media-content">
          {{ task.body }}
        </div>

        <div class="media-right">
          <button class="delete is-medium" @click="confirmDelete"></button>

          <modal-delete
            ref="modal"
            @confirm="deleteTask(task.id)"
          ></modal-delete>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ModalDelete from "../components/modal-delete.vue";

export default {
  name: "Tasks",
  props: {
    task: Object,
  },
  components: {
    ModalDelete,
  },
  methods: {
    setStatus(task_id) {
      axios({
        method: "patch",
        url: "api/tasks/" + task_id + "/",
        data: {
          completed: true,
        },
      });
    },
    deleteTask(task_id) {
      axios({
        method: "delete",
        url: "api/tasks/" + task_id + "/",
      });
    },
    confirmDelete() {
      this.$refs.modal.show = true;
    },
  },
};
</script>