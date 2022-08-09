<template>
  <main>
    <IncidentList
      v-if="currentIncidents.length > 0"
      :incidents="currentIncidents"
      title="Current Incidents"
    />
    <h2>Current Status</h2>
    <StatusCategory
      v-for="category in categories"
      :key="category.title"
      :category="category"
    />
    <IncidentList :incidents="pastIncidents" title="Past Incidents" />
  </main>
</template>

<script>
import StatusCategory from "./StatusCategory.vue";
import IncidentList from "./IncidentList.vue";

const MAX_INCIDENT_AGE = 1000 * 60 * 60 * 24 * 90; // 90 days

export default {
  name: "StatusOverview",
  components: { StatusCategory, IncidentList },
  data() {
    const categories = [
      ...this.$root.$site.pages
        .filter((x) => x.frontmatter.layout === "ComponentDetail")
        .reduce((o, i) => {
          o.add(i.frontmatter.category);
          return o;
        }, new Set([])),
    ]
      .sort()
      .reduce((o, i) => {
        console.log(this.$root.$site);
        o[i] = {
          label: i,
          title: this.$root.$site.themeConfig.componentTitles[i],
          components: [],
        };
        return o;
      }, {});
    const currentIncidents = [];
    const pastIncidents = [];

    this.$root.$site.pages.forEach((x) => {
      if (x.frontmatter.layout === "ComponentDetail") {
        categories[x.frontmatter.category].components.push(x);
      } else if (x.frontmatter.layout === "IncidentDetail") {
        if (x.frontmatter.state !== "closed") {
          currentIncidents.push(x);
        } else {
          const age = Date.now() - new Date(x.frontmatter.created_at);
          if (age < MAX_INCIDENT_AGE) {
            pastIncidents.push(x);
          }
        }
      }
    });

    return {
      categories,
      currentIncidents,
      pastIncidents,
    };
  },
};
</script>
