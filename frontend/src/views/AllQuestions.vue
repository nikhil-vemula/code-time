<script>
import SideNavigation from "../components/SideNavigation.vue";

export default {
  components: { SideNavigation },
  name: "AllQuestions",
  mounted() {
    this.$store.dispatch("getQuestionsForUser");
  },
  computed: {
    questions() {
      return this.$store.getters.getQuestions;
    },
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
            <v-container>
              <v-row>
                <v-col><h1>All questions</h1></v-col>
                <v-col><router-link to="/new-question"><v-btn class="ma-2 float-right" >Add</v-btn></router-link></v-col>
              </v-row>
            </v-container>
            <v-table fixed-header height="80vh">
              <thead>
                <tr>
                  <th class="text-left">Question</th>
                  <th class="text-left">URL</th>
                  <th class="text-left">Difficulty</th>
                  <th class="text-left">Tags</th>
                  <!-- <th class="text-left">Last solved</th> -->
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in questions" :key="item.question_id">
                  <td>
                    <router-link :to="'/question/' + item.question_id">{{
                      item.title
                    }}</router-link>
                  </td>
                  <td>
                    <a :href="item.url">{{ item.url }}</a>
                  </td>
                  <td>{{ item.difficulty_level }}</td>
                  <td>
                    <span v-if="item.tags != ''">
                    <v-chip
                      v-for="tag in item.tags.split(',')"
                      :key="tag"
                      class="mx-1"
                      label
                      size="x-small"
                      >{{ tag }}</v-chip>
                    </span>
                  </td>
                  <!-- <td>1 day ago</td> -->
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>