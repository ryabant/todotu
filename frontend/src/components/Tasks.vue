<template>
  <div>
    <a class="box" @click="confirmEditTask">
      <span v-if="task.completed === true" class="icon has-text-success"
        ><i class="far fa-check-circle"></i
      ></span>
      <div class="card-content">
        <p class="title">
          {{ task.title }}
        </p>
        <div class="field is-grouped is-grouped-multiline">
          <div class="tags are-medium">
            <div class="control">
              <span class="tag" v-for="tag in task.tags" :key="tag.id">{{
                tag
              }}</span>
            </div>
          </div>
        </div>
      </div>
    </a>
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
        this.$refs.modal_edit_task.show = false;
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
          console.log(error);
        });
    },
    confirmEditTask() {
      this.$refs.modal_edit_task.show = true;
    },
  },
};
</script>