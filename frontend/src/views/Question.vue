<script>
import SideNavigation from "../components/SideNavigation.vue";

export default {
  components: { SideNavigation },
  name: "Question",
  data() {
    return {
      question: {
        'title': 'Question'
      }
    };
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
          <v-sheet min-height="80vh" rounded="lg" class="pa-md-4">
            Question {{ $route.params.id }}
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>