<template>
  <div class="column">
    <h2 class="column-title">{{ title }}</h2>

    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Column",
  props: {
    title: {
      type: String,
    },
  },
};
</script>

<style lang="scss">
.column {
  height: 700px;
  width: 300px;
  overflow-y: auto;
  background: #c9c9c9;
  border-radius: 6px;
  margin-bottom: 24px;
}
.column-title {
  font-size: 22px;
  text-align: center;
  padding: 12px;
}
</style>
