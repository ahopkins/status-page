<template>
  <section>
    <h2>{{ title }}</h2>
    <ul v-if="incidents.length > 0">
      <li v-for="incident in incidents" :key="incident.key">
        <router-link
          v-if="incident.frontmatter.permalink"
          :to="incident.frontmatter.permalink"
        >
          {{ incident.title }}
        </router-link>
        <span v-else>{{ incident.title }}</span>
        -
        {{ incident.frontmatter.created_at }}
        <Label color="dddddd">{{ incident.frontmatter.state }}</Label>
      </li>
    </ul>
    <div v-else>No incidents to report. WooHoo!</div>
  </section>
</template>

<script>
import Label from "./Label.vue";
export default {
  name: "IncidentList",
  components: { Label },
  props: ["incidents", "title"],
};
</script>
