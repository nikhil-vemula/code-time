import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/dist/vuetify.min.css';

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'fa',
  },
})

createApp(App)
.use(router)
.use(vuetify)
.mount('#app')
