  <template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="#"
        ><img alt="logo" src="../assets/logo.png"
      /></a>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a @click="logout">Logout</a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import axios from "axios";
export default {
  name: "Nav",
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
  },
};
</script>
