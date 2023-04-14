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
            <v-sheet min-height="70vh" rounded="lg" class="pa-md-4">
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