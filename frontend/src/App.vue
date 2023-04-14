<script>
export default {
  data() {
    return {
      message: 'Hello world!'
    }
  }
}
</script>

<template>
  <v-app id="app">
        <v-content transition="slide-x-transition">
            <router-view></router-view>
        </v-content>
    </v-app>
</template>