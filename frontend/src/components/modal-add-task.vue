<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">New task</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <form v-on:submit.prevent="addTask">
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
          <div
            v-if="
              $route.name !== 'Inbox' &&
              $route.name !== 'Important' &&
              tags.length > 0
            "
            class="field"
          >
            <label class="label">Tags</label>
            <div class="control">
              <div class="select is-multiple">
                <select multiple size="4" v-model="selected">
                  <option v-for="tag in tags" :key="tag.id">
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
          <button class="button is-link" @click="onConfirm">Add Task</button>
        </footer>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalAddTask",
  data() {
    return {
      show: false,
      title: "",
      body: "",
      priority: "Medium",
      selected: [],
      errors: [],
    };
  },
  props: { tags: Object },
  methods: {
    closeModal() {
      this.show = false;
      this.title = "";
      this.body = "";
      this.selected = [];
    },
    onConfirm() {
      const payload = {
        title: this.title,
        body: this.body,
        priority: this.priority,
        tags: this.selected,
      };
      this.$emit("new-task", payload);
      this.title = "";
      this.body = "";
      this.selected = [];
    },
  },
};
</script>