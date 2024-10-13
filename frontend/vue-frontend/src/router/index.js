import { createRouter, createWebHistory } from "vue-router";
import MovieList from '@/components/MovieList.vue';
import MovieDetail from '@/components/MovieDetail.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: "",
        name: "home",
        component: MovieList,
    },
    {
        path: "/movies",
        name: "movies",
        component: MovieList,
    },
    {
        path: "/movies/:id",
        name: "movie",
        component: MovieDetail,
    },
    
  ],
});

export default router;
