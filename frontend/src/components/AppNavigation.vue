<script>
export default {
  name: "AppNavigation",
  data() {
    return {
      appTitle: "Coding Made Easy",
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
  },
  methods: {
    signOut() {
      this.$store.dispatch('userSignOut')
    }
  }
};
</script>

<template>
  <v-app-bar flat>
    <v-container class="fill-height d-flex align-center">
      <!-- <v-avatar class="me-10 ms-4" color="grey-darken-1" size="32"></v-avatar> -->

      <span class="font-weight-bold">Coding Made Easy</span>
      <v-spacer></v-spacer>

      <v-btn variant="text" to="/"> Home </v-btn>

      <v-btn v-if="!isLoggedIn" variant="text" to="/signin">
        Sign in
      </v-btn>
      <v-btn v-else variant="text" @click="signOut">
        Sign out
      </v-btn>
    </v-container>
  </v-app-bar>
</template>