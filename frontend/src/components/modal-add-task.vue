<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Add Task</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <form v-on:submit.prevent="addTask">
        <section class="modal-card-body">
          <div class="field">
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="Task name"
                v-model="title"
              />
            </div>
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
    };
  },
  methods: {
    closeModal() {
      this.show = false;
    },
    onConfirm() {
      const payload = { title: this.title };
      this.$emit("new-task", payload);
      this.title = "";
    },
  },
};
</script>