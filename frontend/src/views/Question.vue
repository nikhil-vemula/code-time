<script>
import SideNavigation from "../components/SideNavigation.vue";

export default {
  components: { SideNavigation },
  name: "Question",
  data() {
    return {
      isFormValid: false,
      isReadOnly: true,
      rules: [],
    };
  },
  mounted() {
    this.$store.dispatch("getQuestion", this.$route.params.id);
  },
  computed: {
    question() {
      return this.$store.getters.getQuestion;
    },
  },
  methods: {
    edit() {
      this.isReadOnly = false;
    },
    save() {
      this.isReadOnly = true;
      this.$refs.form.validate();

      if (!this.isFormValid) return;

      this.$store.dispatch("saveQuestion", {
        title: this.question.title,
        url: this.question.url,
        short_desc: this.question.short_desc,
        description: this.question.description,
        difficulty_level: this.question.difficulty_level,
        tags: this.question.tags,
        notes: this.question.notes,
        question_id: this.question.question_id,
      });
    },
    markSolved() {
      this.$store.dispatch("markQuestion", {
        'question_id': this.question.question_id,
        'solved': true
      })
    },
    markUnsolved() {
      this.$store.dispatch("markQuestion", {
        'question_id': this.question.question_id,
        'solved': false
      })
    }
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
                <v-col>
                  <h1>
                    Question
                    <v-btn @click="markSolved" size="x-small" variant="outlined" prepend-icon="mdi:mdi-check" color="success">Solved</v-btn>
                    <v-btn class="ml-2" @click="markUnsolved" size="x-small" variant="outlined" prepend-icon="mdi:mdi-check" color="error">UN-Solved</v-btn>
                  </h1>
                  
                </v-col>
                <v-col>
                  <v-card-actions class="float-right">
                    <v-spacer></v-spacer>
                    
                    <v-btn
                      @click="edit"
                      v-if="isReadOnly"
                      color="deep-purple-accent-4"
                      >Edit</v-btn
                    >
                    <v-btn @click="save" v-else color="deep-purple-accent-4"
                      >save</v-btn
                    >
                  </v-card-actions>
                </v-col>
              </v-row>
            </v-container>

            <v-form ref="form" v-model="isFormValid" :readonly="isReadOnly">
              <v-container>
                <v-row>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      v-if="!isReadOnly"
                      required
                      v-model="question.title"
                      label="Title"
                      :rules="rules"
                      dense
                      single-line>
                    </v-text-field>
                    <div v-else>
                      <v-label>Title:</v-label> <br/>
                      <p>{{ question.title }}</p>
                    </div>
                  </v-col>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      v-if="!isReadOnly"
                      v-model="question.short_desc"
                      label="Short Description"
                    ></v-text-field>
                    <div v-else>
                      <v-label>Short Description:</v-label> <br/>
                      <p>{{ question.short_desc }}</p>
                    </div>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      required
                      v-if="!isReadOnly"
                      :rules="rules"
                      v-model="question.difficulty_level"
                      label="Difficulty"
                    ></v-text-field>
                    <div v-else>
                      <v-label>Difficulty:</v-label>
                      <p>{{ question.difficulty_level }}</p>
                    </div>
                  </v-col>
                  <v-col cols="12" lg="6">
                    <v-text-field
                      v-if="!isReadOnly"
                      v-model="question.tags"
                      label="Tags"
                      placeholder="Comma seperated"
                    ></v-text-field>
                    <div v-else>
                      <v-label>Tags:</v-label>
                      <span v-if="question.tags">
                      <v-chip
                        v-for="tag in question.tags.split(',')"
                        :key="tag"
                        class="mx-1"
                        label
                        size="small"
                        >{{ tag }}</v-chip>
                      </span>
                    </div>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="12">
                    
                    <v-text-field
                      required
                      v-if="!isReadOnly"
                      :rules="rules"
                      v-model="question.url"
                      label="URL"
                    ></v-text-field>
                    <div v-else>
                      <v-label>Link:</v-label> <br/>
                      <a :href="question.url">{{ question.url }}</a>
                    </div>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="12">
                    <v-textarea
                      counter
                      v-if="!isReadOnly"
                      v-model="question.description"
                      label="Description"
                    ></v-textarea>
                    <div v-else>
                      <v-label>Description:</v-label> <br/>
                      <p v-if="question.description">{{ question.description }}</p>
                      <p v-else>No description</p>
                    </div>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" lg="12">
                    <v-textarea
                      v-if="!isReadOnly"
                      counter
                      v-model="question.notes"
                      label="Notes"
                    ></v-textarea>
                    <div v-else>
                      <v-label>Notes:</v-label> <br/>
                      <p v-if="question.description">{{ question.notes }}</p>
                      <p v-else>No notes</p>
                    </div>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
            <v-divider></v-divider>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>