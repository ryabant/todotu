<template>
  <div class="field">
    <label class="label">Tags</label>
    <div class="control">
      <div class="select">
        <select v-model="selected">
          <option v-for="tag in tags" :key="tag.id">
            {{ tag.name }}
          </option>
        </select>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Tags",
  data() {
    return {
      selected: "",
      tags: Object,
    };
  },
  mounted() {
    this.getTags();
  },
  methods: {
    getTags() {
      axios({
        method: "get",
        url: `api/tags/`,
      })
        .then((response) => {
          this.tags = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>