<script>
import SideNavigation from "../components/SideNavigation.vue";
export default {
  components: { SideNavigation },
  name: "Dashboard",
  data() {
    return {};
  },
};
</script>

<template>
  <v-main class="bg-grey-lighten-3">
    <v-container>
      <v-row>
        <v-col cols="2">
          <side-navigation></side-navigation>
        </v-col>

        <v-col>
          <v-sheet min-height="70vh" rounded="lg">
            <h1>Revise</h1>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>