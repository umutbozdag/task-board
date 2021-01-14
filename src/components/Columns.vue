<template>
  <div>
    <column v-for="col in count" />
  </div>
</template>

<script>
import Column from "./Column.vue";
export default {
  components: { Column },
  name: "Columns",
  props: {
    columnsData: {
      type: Array,
    },
  },
};
</script>

<style></style>
