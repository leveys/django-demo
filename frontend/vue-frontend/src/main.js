import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'
import axios from 'axios'
import router from './router'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import '@mdi/font/css/materialdesignicons.css'

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
})

import { createStore } from 'vuex';
const store = createStore({
  state() {
    return  {
      userId: 1,
    }
  }
})

const app = createApp(App);
app.config.globalProperties.$http = axios

app.use(router)
app.use(vuetify)
app.use(store)
app.mount('#app')