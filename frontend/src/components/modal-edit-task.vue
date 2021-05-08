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
                <select v-model="selected">
                  <option v-for="tag in tags" :key="tag.id">
                    {{ tag }}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <!-- <div class="field">
            <label class="label">Tags</label>
            <div class="control">
              <input
                v-model="tags"
                class="input"
                type="text"
                data-type="tags"
                placeholder="Choose Tags"
              />
            </div>
          </div> -->
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
      selected: "",
    };
  },
  mounted() {
    // const tagsInputs = BulmaTagsInput.attach();
    this.title = this.task.title;
    this.body = this.task.body;
    this.priority = this.task.priority;
    // this.tags = this.task.tags;
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
  },
};
</script>