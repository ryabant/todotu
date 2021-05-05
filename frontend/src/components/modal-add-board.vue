<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Add Board</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <form v-on:submit.prevent="addBoard">
        <section class="modal-card-body">
          <div class="field">
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="Board name"
                v-model="name"
              />
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-link" @click="onConfirm">Add Board</button>
        </footer>
      </form>
    </div>
  </div>
</template>
 
<script>
export default {
  name: "ModalAddBoard",
  data() {
    return {
      show: false,
      name: "",
    };
  },
  methods: {
    closeModal: function () {
      this.show = false;
    },
    onConfirm() {
      const payload = { name: this.name };
      this.$emit("add-board", payload);
      this.name = "";
    },
  },
};
</script>
 