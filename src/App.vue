<template>
  <div id="app">
    <router-view />
    <notifications group="notification" />
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
body {
  margin: 0;
  padding: 0;
}
</style>

<style>
  @import './assets/styles/Home.css';
</style>
