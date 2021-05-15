<template>
  <div>
    <div @mouseover="mouseOver" class="box">
      <div class="tile">
        <div>
          <span v-if="task.completed === true" class="icon has-text-success"
            ><i class="far fa-check-circle"></i
          ></span>
          <span
            v-else-if="task.priority === 'High'"
            class="icon has-text-danger"
            ><i class="fas fa-exclamation-circle"></i
          ></span>
          <span
            v-else-if="task.priority === 'Medium'"
            class="icon has-text-warning"
            ><i class="fas fa-exclamation-circle"></i
          ></span>
        </div>
        <a class="card-content" @click="confirmEditTask">
          <p class="title">
            {{ task.title }}
          </p>
          <div class="field is-grouped is-grouped-multiline">
            <div class="tags are-medium">
              <div class="control">
                <span class="tag" v-for="tag in tags" :key="tag.id">
                  {{ tag.name }}</span
                >
              </div>
            </div>
          </div>
        </a>
        <a class="icon">
          <i
            v-if="task.important === true"
            class="fas fa-star"
            @click="setImportant"
          ></i>
          <i v-else class="far fa-star" @click="setImportant"></i>
        </a>
      </div>
    </div>

    <modal-edit-task
      ref="modal_edit_task"
      :task="task"
      :tags="tags"
      @edit-task="onEditTask"
      @delete-task="confirmDelete"
      @set-status="onSetStatus"
    ></modal-edit-task>
    <modal-delete
      ref="modal_delete_task"
      @confirm="onDeleteTask"
    ></modal-delete>
  </div>
</template>

<script>
import axios from "axios";
import ModalEditTask from "../components/modal-edit-task.vue";
import ModalDelete from "../components/modal-delete.vue";
export default {
  name: "Tasks",
  props: {
    task: Object,
    tags: Object,
  },
  components: { ModalEditTask, ModalDelete },
  methods: {
    onSetStatus() {
      axios({
        method: "patch",
        url: `api/tasks/${this.task.id}/`,
        data: {
          completed: !this.task.completed,
        },
      }).then(() => {
        this.$emit("update-board");
      });
    },
    onDeleteTask() {
      axios({
        method: "delete",
        url: `api/tasks/${this.task.id}/`,
      }).then(() => {
        this.$emit("update-board");
      });
    },
    confirmDelete() {
      this.$refs.modal_delete_task.show = true;
    },
    onEditTask(item) {
      axios({
        method: "patch",
        url: `api/tasks/${this.task.id}/`,
        data: {
          title: item.title,
          body: item.body,
          priority: item.priority,
          tags: item.tags,
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
          this.$emit("edit-task", newTask);
          this.$emit("update-board");
          this.$refs.modal_edit_task.show = false;
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
            this.$refs.modal_add_task.errors = this.errors;
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            this.errors.push("Something went wrong. Please try again");
            this.$refs.modal_add_task.errors = this.errors;
            console.log(JSON.stringify(error));
          }
        });
    },
    confirmEditTask() {
      this.$refs.modal_edit_task.show = true;
    },
    setImportant() {
      axios({
        method: "patch",
        url: `api/tasks/${this.task.id}/`,
        data: {
          important: !this.task.important,
        },
      }).then(() => {
        this.$emit("update-board");
      });
    },
  },
};
</script>