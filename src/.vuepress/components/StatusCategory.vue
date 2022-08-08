<template>
  <div>
    This is a category
    <li v-for="component in category.components" :key="component.key">
      {{ component.title }}:
      {{ component.frontmatter.status }}
    </li>
  </div>
</template>

<script>
export default {
  props: ["category"],
};
</script>
