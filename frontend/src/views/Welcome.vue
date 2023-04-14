<script>
export default {
  name: "Welcome",
};
</script>

<template>
  <v-main class="bg-grey-lighten-3">
    <v-container fluid class="fill-height h-100 back-ground">
      <div class="mx-auto" align="center">
        <h1 class="text-black text-h3 my-4 font-weight-black">
          Coding made easy
        </h1>
        <h2 class="text-black text-h5 my-2">
          Site to track you coding practice
        </h2>
        <v-btn color='primary' flat to="/signin">Sign in</v-btn>
      </div>
    </v-container>
  </v-main>
</template>

<style scoped>
.back-ground {
  background: url("../assets/home-background.jpg");
  background-size: cover;
  width: 100%;
  height: 100%;
}
</style>