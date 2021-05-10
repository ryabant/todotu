<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-content">
      <div class="card">
        <div class="card-content">
          <p v-if="boardName" class="title">
            Delete board: {{ this.boardName }}?
          </p>
          <p v-else class="title">Delete?</p>
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
  name: "ModalDelete",
  props: ["boardName"],
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
 