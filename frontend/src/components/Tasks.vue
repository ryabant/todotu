<template>
  <div class="tasks">
    <div class="box" v-bind:key="task.id">
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

          <modal-window
            ref="modal"
            @confirm="deleteTask(task.id)"
          ></modal-window>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ModalWindow from "../components/modal-window.vue";

export default {
  name: "Tasks",
  data() {
    return {};
  },
  props: {
    task: Object,
  },
  components: {
    ModalWindow,
  },
  mounted() {},
  computed: {},
  methods: {
    async setStatus(task_id) {
      await axios({
        method: "patch",
        url: "api/tasks/" + task_id + "/",
        data: {
          completed: true,
        },
      });
    },
    async deleteTask(task_id) {
      await axios({
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