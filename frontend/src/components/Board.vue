<template>
  <div>
    <div>
      <p>{{ board.name }}</p>
    </div>
    <Tasks
      v-for="task in board.tasks"
      v-bind:key="task.id"
      v-bind:task="task"
    />
  </div>
</template>

<script>
import axios from "axios";
import Tasks from "../components/Tasks.vue";

export default {
  name: "Board",
  components: {
    Tasks,
  },
  data() {
    return {
      board: {
        tasks: [],
      },
    };
  },
  mounted() {
    this.getBoard();
  },

  methods: {
    async getBoard() {
      const id = this.$route.params.id;
      await axios({
        method: "get",
        url: `api/boards/${id}`,
      })
        .then((response) => {
          this.board = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>