<template>
  <span class="label" :style="styleObject">
    <slot />
  </span>
</template>

<script>
export default {
  name: "Label",
  props: ["color"],
  data() {
    const r = parseInt(this.color.substr(0, 2), 16);
    const g = parseInt(this.color.substr(2, 2), 16);
    const b = parseInt(this.color.substr(4, 2), 16);
    const yiq = (r * 299 + g * 587 + b * 114) / 1000;
    const textColor = yiq >= 128 ? "black" : "white";
    return {
      styleObject: {
        backgroundColor: `#${this.color}`,
        color: textColor,
      },
    };
  },
};
</script>

<style scoped>
.label {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  font-size: 0.7rem;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 0.25rem;
}
</style>
