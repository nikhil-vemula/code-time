<script>
import SideNavigation from "../components/SideNavigation.vue";

export default {
  components: { SideNavigation },
  name: "Question",
  data() {
    return {
      isFormValid: false,
      question: {
        title: "",
        url: "",
        short_desc: "",
        description: "",
        difficulty_level: "",
        tags: "",
        notes: "",
      },
      rules: [
        (value) => {
          if (value) return true;
          return "Field can not be empty.";
        },
      ],
    };
  },
  methods: {
    save() {
      this.$refs.form.validate();

      if (!this.isFormValid) 
        return;

      this.$store.dispatch('saveQuestion', {
        title: this.question.title,
        url: this.question.url,
        short_desc: this.question.short_desc,
        description: this.question.description,
        difficulty_level: this.question.difficulty_level,
        tags: this.question.tags,
        notes: this.question.notes,
      })
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
            <h1 class="mb-4">New Question</h1>
            <v-form ref="form" v-model="isFormValid">
              <v-container>
                <v-row>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      required
                      v-model="question.title"
                      label="Title"
                      :rules="rules"
                      dense
                      single-line
                    >
                    </v-text-field>
                  </v-col>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      v-model="question.short_desc"
                      label="Short Description"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      required
                      :rules="rules"
                      v-model="question.difficulty_level"
                      label="Difficulty"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      v-model="question.tags"
                      label="Tags"
                      placeholder="Comma seperated"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="12">
                    <v-text-field
                      required
                      :rules="rules"
                      v-model="question.url"
                      label="URL"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="12">
                    <v-textarea
                      counter
                      v-model="question.description"
                      label="Description"
                    ></v-textarea>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="12">
                    <v-textarea
                      counter
                      v-model="question.notes"
                      label="Notes"
                    ></v-textarea>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="save" color="deep-purple-accent-4"> Save</v-btn>
            </v-card-actions>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>