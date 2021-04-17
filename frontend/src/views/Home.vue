<template>


<div class="home">
<div class="columns">
  <div class="column is-6 is-offset-3">
  <form v-on:submit.prevent="addTask">
  <div class='field'>
    <div class="control">
      <input class="input" type="text" placeholder="Text input" v-model="body">
    </div>
  </div>
  <div class="field">
  <p class="control">
    <button class="button is-success">
      Add Task
    </button>
  </p>
</div>
  </form>
  </div>
</div>

<div class="columns">
  <div class="column is-6 is-offset-3">
  <div class='cards'>
    <div class="card" v-for="task in completedTasks" v-bind:key="task.id">
      <div class="card-content">
        <div class="columns">
          <div class="column is-four-fifths">
            {{ task.body }}
          </div>
          <div class="column">
            <button class="button is-success" @click="setStatus(task.id)">Done</button>
          </div>
          <div class="column">
            <button class="button is-danger" @click="showModal">Delete</button>
                <modal
                  v-show="isModalVisible"
                  @close="closeModal"
                />
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</div>
</div>




</template>

<script>
import axios from 'axios'
import modal from "../components/modal.vue";

export default {
  name: "Home",
  components: {
    modal
   },
  data() {
    return {
      tasks: [],
      body: '',
      isModalVisible: false,
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
      await axios({
        method: 'get',
        url: 'api/tasks/',
      })
      .then(response => {
        this.tasks = response.data;
      }).catch(error => {
        console.log(error)
      })
    },
    async addTask() {
      if (this.body) {
        await axios({
          method: "post",
          url: 'api/tasks/',
          data: {
            body: this.body,
            board: 1
          }
        })
        .then(response => {
          let newTask = {
            "id": response.data.id,
            "body": this.body,
          }
          this.tasks.unshift(newTask)

          this.body = ''
        })
        .catch(error => {
          console.log(error)
        })
      }
    },
    async setStatus(task_id) {
      await axios({
        method: "patch",
        url: 'api/tasks/' + task_id + '/',
        data: {
            completed: true,
          }
      })
      this.getTasks()
    },
    async deleteTask(task_id) {
      await axios({
        method: "delete",
        url: 'api/tasks/' + task_id + '/',
      })
      this.getTasks()
    },
    showModal() {
      this.isModalVisible = true
    },
    closeModal() {
      this.isModalVisible = false
    },
  }
}
</script>