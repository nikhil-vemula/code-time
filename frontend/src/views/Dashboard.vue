<script>
import SideNavigation from "../components/SideNavigation.vue";
import { Bar } from "vue-chartjs";

export default {
  components: { SideNavigation },
  name: "Dashboard",
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch('fetchProblemsCount')
    this.$store.dispatch('fetchSolvedProblemsCount')
    this.$store.dispatch('fetchReviseQuestions')
  },
  computed: {
    reviseQuestions() {
      return this.$store.getters.getReviseQuestions
    },
    problemsCount() {
      return this.$store.getters.getProblemsCount
    },
    solvedProblemsCount() {
      return this.$store.getters.getSolvedProblemsCount
    }
  }
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
          <v-sheet min-height="70vh" rounded="lg" class="pa-md-4">
            <!-- Metrics -->
            <v-container fluid>
              <v-row dense align="center">
                <v-card class="ma-4" width="45%">
                  <v-card-title><span class="font-weight-black">All questions</span></v-card-title>
                  <v-card-text><span class="text-h4">{{ problemsCount }}</span></v-card-text>
                </v-card>
                <v-card class="ma-4" width="45%">
                  <v-card-title><span class="font-weight-black">Solved questions</span></v-card-title>
                  <v-card-text><span class="text-h4">{{ solvedProblemsCount }}</span></v-card-text>
                </v-card>
              </v-row>
            </v-container>

            <!-- Revise -->
            <h1>Revise</h1>
            <v-table fixed-header height="40vh">
              <thead>
                <tr>
                  <th class="text-left">Question</th>
                  <th class="text-left">Link</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in reviseQuestions" :key="item.question_id">
                  <td><router-link :to="'/question/' + item.question_id">{{ item.title }}</router-link></td>
                  <td><a :href="item.url">{{ item.url }} </a></td>
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>