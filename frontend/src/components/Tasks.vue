<template>
  <div>
    <a class="box" @click="confirmEditTask">
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
    ></modal-edit-task>
  </div>
</template>

<script>
import axios from "axios";
import ModalEditTask from "../components/modal-edit-task.vue";
export default {
  name: "Tasks",
  props: {
    task: Object,
    tags: Object,
  },
  components: { ModalEditTask },
  methods: {
    // setStatus(task_id) {
    //   axios({
    //     method: "patch",
    //     url: "api/tasks/" + task_id + "/",
    //     data: {
    //       completed: true,
    //     },
    //   }).then(() => {
    //     this.$emit("update-board");
    //   });
    // },
    // deleteTask(task_id) {
    //   axios({
    //     method: "delete",
    //     url: "api/tasks/" + task_id + "/",
    //   }).then(() => {
    //     this.$emit("update-board");
    //   });
    // },
    // confirmDelete() {
    //   this.$refs.modal.show = true;
    // },
    onEditTask(item) {
      axios({
        method: "patch",
        url: `api/tasks/${this.task.id}/`,
        data: {
          title: item.title,
          body: item.body,
          priority: item.priority,
        },
      })
        .then(() => {
          // let newTask = {
          //   id: response.data.id,
          //   title: item.title,
          //   body: item.body,
          //   priority: item.priority,
          //   board: this.boardId,
          // };
          // this.$emit("edit-task", newTask);
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