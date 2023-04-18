<script>
export default {
  name: "Signin",
  data() {
    return {
      isFormValid: false,
      email: "",
      emailRules: [
        (value) => {
          if (value) return true;

          return "E-mail is required.";
        },
        value => {
          if (/.+@.+\..+/.test(value)) return true

          return 'E-mail must be valid.'
        },
      ],
      password: "",
      passwordRules: [
        (value) => {
          if (value) return true;

          return "Password is required.";
        },
      ],
    };
  },
  methods: {
    async submit(event) {
      this.$refs.form.validate();
      if (!this.isFormValid)
        return;
      
      this.$store.commit("setLoginFailed", false);
      this.$store.dispatch("userLogin", {
        email: this.email,
        password: this.password,
      });
    },
  },
  computed: {
    isLoginFailed() {
      return this.$store.getters.isLoginFailed;
    },
  },
};
</script>

<template>
  <v-main class="bg-grey-lighten-3">
    <div class="d-flex align-center justify-center" style="height: 50vh">
      <v-sheet width="400" class="mx-auto pa-4" rounded="lg">
        <v-alert
          v-model="isLoginFailed"
          class="my-2"
          color="error"
          text="Incorrect user or password"
          variant="tonal"
        ></v-alert>
        <v-form ref="form" @submit.prevent="submit" v-model="isFormValid">
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
          ></v-text-field>
          <v-text-field
            v-model="password"
            :rules="passwordRules"
            label="Password"
            type="password"
          ></v-text-field>
          <v-btn
            type="submit"
            color="primary"
            block
            class="mt-2"
            >Sign in</v-btn
          >
        </v-form>
        <div class="mt-2">
          <p class="text-body-2">
            Don't have an account? <router-link to="/signup">Sign Up</router-link>
          </p>
        </div>
      </v-sheet>
    </div>
  </v-main>
</template>