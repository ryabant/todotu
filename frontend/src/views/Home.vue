<template>
  <div class='home'>
    <div class="card">
      <div class="card-content" v-for="task in completedTasks" v-bind:key="task.id">{{ task.body }}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Home",
  data() {
    return {
      tasks: []
    }
  },
  mounted () {
    this.getTasks()
  },
  computed: {
    completedTasks() {
      return this.tasks.filter(task => {
        return !task.completed;
      })
    }
  },
  methods: {
    async getTasks() {
      axios.get('api/tasks/').
      then(response=> {
        this.tasks = response.data;
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>