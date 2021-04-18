<template>
  <transition name="modal-fade">
    <div class="modal">
      <div class="modal-background"></div>
      <div class="modal-content">some random text</div>
      <button class="modal-close is-large" aria-label="close"></button>
    </div>
  </transition>
</template>


<script>
export default {
  name: "modal",
};
</script>