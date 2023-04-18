<script>
import AppNavigation from './components/AppNavigation.vue'

export default {
  components: { AppNavigation },
  mounted() {
    if (localStorage) {
      let user = localStorage.getItem('user')
      if (user != null) {
        user = JSON.parse(user)
        this.$store.commit('setUser', user)
        this.$store.commit('setLoggedIn', true)
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