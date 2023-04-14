<script>
import AppNavigation from './components/AppNavigation.vue'

export default {
  components: { AppNavigation }
}
</script>

<template>
  <v-app id="app">
    <app-navigation></app-navigation>
    <router-view></router-view>
  </v-app>
</template>