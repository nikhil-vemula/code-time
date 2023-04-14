<script>
import SideNavigation from "../components/SideNavigation.vue";
import { Bar } from "vue-chartjs";

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
          <v-sheet min-height="70vh" rounded="lg" class="pa-md-4">
            <!-- Metrics -->
            <v-container fluid>
              <v-row dense align="center">
                <v-card class="ma-4" width="45%">
                  <v-card-title><span class="font-weight-black">All questions</span></v-card-title>
                  <v-card-text><span class="text-h4">200</span></v-card-text>
                </v-card>
                <v-card class="ma-4" width="45%">
                  <v-card-title><span class="font-weight-black">Solved questions</span></v-card-title>
                  <v-card-text><span class="text-h4">50</span></v-card-text>
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
                <tr v-for="item in 100" :key="item.title">
                  <td>Question {{ item }}</td>
                  <td>Question {{ item }} link</td>
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>