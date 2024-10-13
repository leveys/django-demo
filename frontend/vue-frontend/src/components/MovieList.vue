<style scoped>
  .five-cols {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    min-height: 1000px;
  }

  .text.single-line {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .content {
    min-width: 1000px;
  }
</style>

<script>
export default {
  data() {
    return {
      title: "",
      movies: [],
      total_movie_count: 0,
      prev_url: null,
      next_url: null,
      pagination_offset: 0,
      movie_count_str: "loading...",
    };
  },
  methods: {
    async getMovies() {		
      this.movie_count_str = "loading..."	
      var url = `http://0.0.0.0:8000${this.$route.fullPath}`
      if (this.$route.query.ordering === undefined) {
        if (Object.keys(this.$route.query).length === 0) {
          url += '?ordering=id'
        } else {
          url += '&ordering=id'
        }
      }
      if (this.$route.query.search !== undefined) {
        this.title = `You searched for '${this.$route.query.search}'`
      } else {
        this.title = 'All movies'
      }
      try {
        await this.$http
          .get(url)
          .then((response) => {
            this.movies = response.data.results
            this.total_movie_count = response.data.count
            this.prev_url = response.data.previous
            this.next_url = response.data.next
            if (this.$route.query.offset) {
              this.pagination_offset = parseInt(this.$route.query.offset)
            } else {
              this.pagination_offset = 0
            }
            var movie_count = this.movies.length
            if (movie_count == 0) {
                this.movie_count_str = `no movies found`
            } else {
                this.movie_count_str = `showing ${this.pagination_offset + 1} - ${this.pagination_offset + movie_count} out of ${this.total_movie_count} movies`
            }
        })
      } catch (error) {
        console.log(error);
      }
    },
    async prev() {
        if (this.prev_url != null) {
            this.$router.push(this.prev_url.substring(19))
        }
    },
    async next() {
        if (this.next_url != null) {
            this.$router.push(this.next_url.substring(19))
        }
    },
    setMoviePoster(movie) {
        var img = document.getElementById('movie_poster_' + movie.id)
        if (img != null && movie.poster_path.length > 0) {
            img.src = `https://image.tmdb.org/t/p/original${movie.poster_path}`
        }
    }
  },
	created() {
		this.getMovies()
	},
  watch: {
    $route(to, from) {
        this.getMovies()
    }
  },
  computed: {
    next_btn_disabled: {
        get() {
            return this.next_url === null
        }
    },
    prev_btn_disabled: {
        get() {
            return this.prev_url === null
        }
    }
  }
}
</script>

<template>
  <div class="content">
    <h1>{{ this.title }}</h1>
    <h4>{{  this.movie_count_str }}</h4> 
    <v-btn @click="prev()" :disabled="prev_btn_disabled"><<</v-btn> 
    <v-btn @click="next()" :disabled="next_btn_disabled">>></v-btn>

    <v-container>
      <v-row class="five-cols">
        <v-col v-for="movie in movies" :key="movie.id">
          <v-card max-width="185px" variant="flat">
            <h3 class="text single-line">{{ movie.title }}</h3>
            <router-link :to="{ name: 'movie', params: { id: movie.id } }"> 
              <img :id="'movie_poster_' + movie.id"
                  src="@/assets/image_not_found.png"
                  :on-load="setMoviePoster(movie)"
                  width="185px" height="278px" >
              <v-tooltip activator="parent" location="bottom">
                {{ movie.title }}
              </v-tooltip>
            </router-link>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-btn @click="prev()" :disabled="prev_btn_disabled"><<</v-btn> 
    <v-btn @click="next()" :disabled="next_btn_disabled">>></v-btn>
  </div>
</template>