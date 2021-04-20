<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-content">
      <div class="card">
        <div class="card-content">
          <p class="title">Are you sure?</p>
        </div>
        <div class="card-content">
          <button class="button is-danger" @click="onConfirm">Delete</button>
          <button class="button" @click="closeModal">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>
 
<script>
export default {
  name: "ModalWindow",
  data: function () {
    return {
      show: false,
    };
  },
  methods: {
    closeModal: function () {
      this.show = false;
    },
    onConfirm() {
      this.$emit("confirm");
    },
  },
};
</script>
 