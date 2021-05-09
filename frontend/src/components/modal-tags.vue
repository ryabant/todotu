<template>
  <div class="modal" v-bind:class="{ 'is-active': show }">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Tags</p>
        <button class="delete" aria-label="close" @click="closeModal"></button>
      </header>
      <section class="modal-card-body">
        <div class="field is-grouped is-grouped-multiline">
          <div v-for="tag in tags" :key="tag.id" class="control">
            <div class="tags has-addons">
              <span class="tag is-medium">{{ tag.name }}</span>
              <span
                class="tag is-delete is-medium"
                @click="deleteTag(tag.id)"
              ></span>
            </div>
          </div>
        </div>
        <form v-on:submit.prevent="addTag">
          <div class="field">
            <label class="label">New tag</label>
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="Task name"
                v-model="name"
              />
            </div>
          </div>
          <button class="button is-link">Add Tag</button>
        </form>
      </section>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "ModalTags",
  props: { tags: Object },
  data() {
    return {
      show: false,
      name: "",
    };
  },
  methods: {
    closeModal() {
      this.show = false;
    },
    addTag() {
      if (this.name) {
        axios({
          method: "post",
          url: "api/tags/",
          data: {
            name: this.name,
          },
        })
          .then(() => {
            this.$emit("update-tags");
            this.name = "";
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    deleteTag(tagId) {
      axios({
        method: "delete",
        url: "api/tags/" + tagId + "/",
      }).then(() => {
        this.$emit("update-tags");
      });
    },
  },
};
</script>