<script>
import SideNavigation from "../components/SideNavigation.vue";

export default {
  components: { SideNavigation },
  name: "AllQuestions",
  data() {
    return {
      questions: [
        { id: 1, title: "Question 1", link: "/question/1" },
        { id: 2, title: "Question 2", link: "/question/2" },
        { id: 3, title: "Question 3", link: "/question/3" },
        { id: 4, title: "Question 4", link: "/question/4" },
        { id: 5, title: "Question 5", link: "/question/5" },
        { id: 5, title: "Question 5", link: "/question/5" },
      ],
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
            <v-table fixed-header height="80vh">
              <thead>
                <tr>
                  <th class="text-left">Question</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in 100" :key="item.title">
                  <td><router-link :to="'/question/' + item">Question {{ item }}</router-link></td>
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>