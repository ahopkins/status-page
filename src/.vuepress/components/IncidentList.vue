<template>
  <section>
    <h3>{{ title }}</h3>
    <li v-for="incident in incidents" :key="incident.key">
      {{ incident.title }} - {{ incident.frontmatter.reported }}
    </li>
  </section>
</template>

<script>
export default {
  props: ["incidents", "title"],
};
</script>
