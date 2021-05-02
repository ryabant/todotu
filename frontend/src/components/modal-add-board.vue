<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-content">
      <div class="card">
        <div class="card-content">
          <p class="title">Add Board</p>
        </div>
        <div class="card-content">
          <form class="box" v-on:submit.prevent="addBoard">
            <div class="field">
              <div class="control">
                <input
                  class="input"
                  type="text"
                  placeholder="Text input"
                  v-model="name"
                />
              </div>
            </div>
            <div class="field">
              <p class="control">
                <button class="button is-link" @click="onConfirm">
                  Add Board
                </button>
              </p>
            </div>
          </form>
        </div>
        <div class="card-content">
          <button class="button" @click="closeModal">Cancel</button>
        </div>
      </div>
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
 