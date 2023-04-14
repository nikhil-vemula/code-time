<script>
export default {
  name: "SideNavigation",
  data() {
    return {
      items: [
        { text: "Dashboard", to: "/dashboard" },
        { text: "All Questions", to: "/allquestions"}
      ],
    };
  },
};
</script>

<template>
  <v-sheet rounded="lg">
    <v-list rounded="lg">
      <v-list-item v-for="item in items" :key="item.text" :to="item.to" link>
        <v-list-item-title> {{ item.text }} </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-sheet>
</template>