<template>
  <div class="box">
    <h4>{{ category.title }}</h4>
    <li v-for="component in category.components" :key="component.key">
      <router-link v-if="component.path" :to="component.path">{{
        component.title
      }}</router-link>
      <span v-else>{{ component.title }}</span>
      {{ component.frontmatter.status }}
      (uptime: {{ component.frontmatter.uptime }}%)
    </li>
  </div>
</template>

<script>
export default {
  name: "StatusCategory",
  props: ["category"],
};
</script>

<style scoped>
.box {
  border: 1px solid black;
  padding: 1em;
}
</style>
