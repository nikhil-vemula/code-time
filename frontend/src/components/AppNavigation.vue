<script>
export default {
  name: "AppNavigation",
  data() {
    return {
      appTitle: "Coding Made Easy"
    };
  },
};
</script>

<template>
  <v-app-bar flat>
    <v-container class="fill-height d-flex align-center">
        <v-avatar
          class="me-10 ms-4"
          color="grey-darken-1"
          size="32"
        ></v-avatar>

        <v-spacer></v-spacer>

        <v-btn
          variant="text"
          to="/">
          Home
        </v-btn>

        <v-btn
          variant="text"
          to="/signin">
          Sign in
        </v-btn>
      </v-container>
    </v-app-bar>
</template>