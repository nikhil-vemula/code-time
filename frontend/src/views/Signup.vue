<script>
export default {
  name: "Signup",
  data() {
    return {
      isFormValid: false,
      firstname: "",
      lastname: "",
      email: "",
      password: "",
      nameRules: [
        (value) => {
          if (value) return true;

          return "First name is required";
        },
      ],
      emailRules: [
        (value) => {
          if (value) return true;

          return "E-mail is required.";
        },
        (value) => {
          if (/.+@.+\..+/.test(value)) return true;

          return "E-mail must be valid.";
        },
      ],
      passwordRules: [
        (value) => {
          if (value) return true;

          return "Password is required.";
        },
      ],
    };
  },
  methods: {
    submit() {
      console.log("called", this.isFormValid);
      this.$refs.form.validate();

      if (!this.isFormValid) return;

      this.$store.dispatch("createUser", {
        first_name: this.firstname,
        last_name: this.lastname,
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>

<template>
  <v-main class="bg-grey-lighten-3">
    <div class="d-flex align-center justify-center" style="height: 70vh">
      <v-sheet width="400" class="mx-auto pa-4" rounded="lg">
        <v-form ref="form" @submit.prevent="submit" v-model="isFormValid">
          <v-text-field
            required
            :rules="nameRules"
            v-model="firstname"
            label="First Name"
          ></v-text-field>
          <v-text-field v-model="lastname" label="Last Name"></v-text-field>
          <v-text-field
            required
            v-model="email"
            :rules="emailRules"
            label="E-mail"
          ></v-text-field>
          <v-text-field
            required
            v-model="password"
            :rules="passwordRules"
            label="Password"
            type="password"
          ></v-text-field>
          <v-btn type="submit" color="primary" block class="mt-2">
            Sign up
          </v-btn>
        </v-form>
      </v-sheet>
    </div>
  </v-main>
</template>