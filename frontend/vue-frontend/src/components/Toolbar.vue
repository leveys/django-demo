<script>
export default {
  data() {
    return {
      searchterm: "",
      userText: "",
      userRules: [
        v => (v.length === 0 || this.isNumeric(v)) || "User id must be an integer"
      ]
    }
  },
  methods: {
    searchMovies() {
      this.$router.push({name: 'movies', query: { search: this.searchterm }})
      this.searchterm = ''
    },
    isNumeric(value) {
      return /^\d+$/.test(value);
    },
    async changeUser() {
      if (this.isNumeric(this.userText)) {
        this.$store.state.userId = this.userText
        try {
            await this.$http
            .get(`http://0.0.0.0:8000/user/?id=${this.userText}`)
            .then((response) => {
                document.getElementById("user_exists_alert").style.display = "none"
            })
        } catch(error) {
            document.getElementById("user_exists_alert").style.display = "block"
        }
        this.userText = ""
      }
    }
  },
}
</script>

<template>
    <v-toolbar title="Movie demo app" dark>
      <v-toolbar-items>
        <v-text-field
          prepend-inner-icon="mdi-magnify"
          placeholder="Search movies"
          type="input"
          v-model="searchterm"
          v-on:keyup.enter="searchMovies"
          single-line
        ></v-text-field>
        <v-btn :to="'/'"
            variant="flat"
            icon="mdi-home">
        </v-btn>
        <!-- <v-btn :to="'/movies'" icon="mdi-movie-open"></v-btn> -->
      </v-toolbar-items>
    </v-toolbar>
</template>

<style scoped>
.v-text-field{
  width: 400px;
}
.v-alert{
    display: none;
}
</style>