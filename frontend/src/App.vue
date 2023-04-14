<script>
export default {
  data() {
    return {
      message: 'Hello world!'
    }
  }
}
</script>

<template>
  <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/signup">Signup</router-link>
  </div>
  <router-view />
</template>