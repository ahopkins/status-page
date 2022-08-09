<template>
  <div class="theme-container no-sidebar">
    <Navbar />

    <main class="page component">
      <div class="go-back">
        <div class="right">
          {{ this.$root.$page.frontmatter.status }}
          (uptime: {{ this.$root.$page.frontmatter.uptime }}%)
        </div>
        <router-link to="/">Go back</router-link>
      </div>
      <div class="theme-default-content">
        <Content />
        <IncidentList :incidents="incidents" title="Incidents" />
      </div>
    </main>
  </div>
</template>

<script>
import Navbar from "@theme/components/Navbar.vue";
import IncidentList from "./IncidentList.vue";
export default {
  name: "ComponentDetail",
  components: {
    Navbar,
    IncidentList,
  },
  data() {
    const component = this.$root.$page.frontmatter.component;
    const incidents = this.$root.$site.pages.reduce((o, i) => {
      if (
        i.frontmatter.layout === "IncidentDetail" &&
        i.frontmatter.component === component
      ) {
        o.push(i);
      }
      return o;
    }, []);
    return {
      incidents,
    };
  },
};
</script>

<style>
.go-back {
  max-width: 740px;
  margin: 100px auto 0;
}
.right {
  float: right;
}
.component .theme-default-content:not(.custom) {
  padding-top: 0;
}
</style>
