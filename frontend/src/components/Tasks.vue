<template>
  <div class="home">
    <div class="columns">
      <div class="column">
        <div class="cards">
          <div class="card" v-if="!task.completed" v-bind:key="task.id">
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