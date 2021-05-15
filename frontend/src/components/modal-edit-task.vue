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
          <div class="level">
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
            <div class="level-left">
              <div class="container">
                <div class="mb-1">
                  <button
                    v-if="!task.completed"
                    class="button"
                    @click="onConfirmStatus"
                  >
                    <span class="icon">
                      <i class="fas fa-check"></i>
                    </span>
                    <span>Complete</span>
                  </button>
                  <button
                    v-else
                    class="button is-success"
                    @click="onConfirmStatus"
                  >
                    <span class="icon">
                      <i class="fas fa-check"></i>
                    </span>
                    <span>Complete</span>
                  </button>
                </div>
                <div class="mb-1">
                  <button class="button" @click="onConfirmDeleteTask">
                    <span class="icon">
                      <i class="fas fa-trash"></i>
                    </span>
                    <span>Delete</span>
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div v-if="$route.name !== 'Inbox' && tags.length > 0" class="field">
            <label class="label">Tags</label>
            <div class="control">
              <div class="select is-multiple">
                <select multiple size="4" v-model="selected">
                  <option v-for="tag in filterTags" :key="tag.id">
                    {{ tag.id }}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-link" @click="onConfirm">Save</button>
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
      important: "",
      myday: "",
      selected: [],
      errors: [],
    };
  },
  computed: {
    filterTags() {
      return this.tags.filter((tag) => tag.board === this.task.board);
    },
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
        important: this.important,
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