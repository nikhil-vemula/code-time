<script>
import AppNavigation from './components/AppNavigation.vue'

export default {
  components: { AppNavigation },
  beforeMount() {
    if (localStorage) {
      let user = localStorage.getItem('user')
      if (user != null) {
        user = JSON.parse(user)
        this.$store.commit('setUser', user)
        this.$store.commit('setLoggedIn', true)
      } else {
        this.$store.commit('setUser', null)
        this.$store.commit('setLoggedIn', false)
      }
    }
  }
}
</script>

<template>
  <v-app id="app">
    <app-navigation></app-navigation>
    <router-view></router-view>
  </v-app>
</template>