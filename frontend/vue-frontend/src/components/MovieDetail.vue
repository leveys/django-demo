<style scoped>
  #wrapper {
    width: 1000px;
    overflow: hidden; 
  }
  #left {
    width: 500px;
    float:left;
  }
  #right {
    margin-top: 20px;
    padding: 20px;
    overflow: hidden;
  }
</style>

<script>
export default {
  data() {
    return {
      movie: {},
    }
  },
  methods: {
    async getMovie(id) {
      try {
        await this.$http
          .get(`http://0.0.0.0:8000/movies/${id}`)
          .then((response) => {
            this.movie = response.data
            this.setMoviePoster(this.movie, true)
        })
      } catch (error) {
        console.log(error)
      }
    },
    setMoviePoster(movie, is_main) {
      var element_id = is_main ? 'main_movie_poster' : `movie_poster_${movie.id}`
      var img = document.getElementById(element_id)
      if (img != null && movie.poster_path.length > 0) {
          img.src = `https://image.tmdb.org/t/p/original${movie.poster_path}`
      }
    },
  },
  created() {
    // Fetch movie on page load
    this.getMovie(this.$route.params.id)
  },
  computed: {
    runtime: {
      get() {
        return `${Math.floor(this.movie.runtime/60)}h ${this.movie.runtime%60}m`
      }
    },
    release_date: {
      get() {
        var date = new Date(this.movie.release_date)
        return date.toLocaleDateString('nl-BE')
      }
    },
    genres: {
      get() {
        if (this.movie.genres != undefined) {
          return JSON.parse(this.movie.genres.replace(/'/g, '"')).map(element => element.name)
        }
      }
    },
    languages: {
      get() {
        if (this.movie.spoken_languages != undefined) {
          return JSON.parse(this.movie.spoken_languages.replace(/'/g, '"')).map(element => element.name)
        }
      }
    },
  },
}
</script>

<template>
  <div class="content">
    <div id="wrapper">
      <div id="left">
        <img id="main_movie_poster"
            src="@/assets/image_not_found.png"
            :on-error="this.src='@/assets/image_not_found.png'"
            width="500px" height="750px" >
      </div>
      <div id="right">
        <h1>{{ movie.title }}</h1>
        <v-chip v-for="genre in genres">
          {{ genre }}
        </v-chip>
        <br><br>
        <p>{{ movie.overview }}</p>
        <br>
        <p>runtime: {{ runtime }}</p>
        <br>
        <p>released: {{ release_date }}</p>
        <br>
        <v-chip v-for="lang in languages">
          {{ lang }}
        </v-chip>
      </div>
    </div>
  </div>
</template>