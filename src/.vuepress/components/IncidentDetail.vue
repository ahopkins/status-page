<template>
  <div class="theme-container no-sidebar">
    <Navbar />

    <main class="page incident">
      <div class="go-back">
        <router-link to="/">Go back</router-link>
      </div>
      <Content class="theme-default-content" />
    </main>
  </div>
</template>

<script>
import Navbar from "@theme/components/Navbar.vue";
export default {
  name: "IncidentDetail",
  components: {
    Navbar,
  },
};
</script>

<style>
.go-back {
  max-width: 740px;
  margin: 100px auto 0;
}
.incident .theme-default-content:not(.custom) {
  padding-top: 0;
}
</style>
