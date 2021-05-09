<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Edit task</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <form v-on:submit.prevent="onEditTask">
        <section class="modal-card-body">
          <div class="field">
            <label class="label">Title</label>
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="Task name"
                v-model="title"
              />
            </div>
          </div>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <textarea
                class="textarea"
                type="text"
                placeholder="Task description"
                v-model="body"
              />
            </div>
          </div>

          <div class="field">
            <label class="label">Priority</label>
            <div class="control">
              <div class="select">
                <select v-model="priority">
                  <option>High</option>
                  <option>Medium</option>
                  <option>Low</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label class="label">Tags</label>
            <div class="control">
              <div class="select is-multiple">
                <select multiple size="4" v-model="selected">
                  <option v-for="tag in tags" :key="tag.id">
                    {{ tag.name }}
                  </option>
                </select>
                <span>Выбрано: {{ selected }}</span>
              </div>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-link" @click="onConfirm">Save</button>
          <button class="button is-danger" @click="onConfirmDeleteTask">
            <i class="fas fa-trash"></i>
          </button>
          <button class="button is-success" @click="onConfirmStatus">
            <i class="fas fa-check"></i>
          </button>
        </footer>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalEditTask",
  props: {
    task: Object,
    tags: Object,
  },
  data() {
    return {
      show: false,
      title: "",
      body: "",
      priority: "",
      selected: [],
    };
  },
  mounted() {
    this.title = this.task.title;
    this.body = this.task.body;
    this.priority = this.task.priority;
    this.selected = this.task.tags;
  },
  methods: {
    closeModal() {
      this.show = false;
    },
    onConfirm() {
      const payload = {
        title: this.title,
        body: this.body,
        priority: this.priority,
        tags: this.selected,
      };
      this.$emit("edit-task", payload);
    },
    onConfirmDeleteTask() {
      this.$emit("delete-task");
    },
    onConfirmStatus() {
      this.$emit("set-status");
    },
  },
};
</script>