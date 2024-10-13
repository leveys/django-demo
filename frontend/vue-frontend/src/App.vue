<template>
  <v-container>
    <Toolbar class="toolbar"/>
    <router-view class="router-view" />
  </v-container>
</template>
  
<script>
    import MovieList from './components/MovieList.vue';
    import MovieDetail from './components/MovieDetail.vue';
    import HomePage from './components/HomePage.vue'
    import Toolbar from './components/Toolbar.vue';

    export default {
        name: 'App',
        components: {
            HomePage,
            MovieList,
            MovieDetail,
            Toolbar
        }
    }
</script>

<style scoped>
.toolbar {
    position: fixed;
    left: 0px;
    top: 0px;
    z-index: 999 !important;
}
.router-view {
    position: relative;
    top: 50px;
    padding-bottom: 50px;
    padding-top: 20px;
}
</style>