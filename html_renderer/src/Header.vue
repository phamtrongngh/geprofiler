<template>
  <div class="header">
    <div class="title">geprofiler</div>
  </div>
</template>
<script>
export default {
  name: "Header",
};
</script>
<style scoped>
.header {
  background-color: #292f32;
}
.title {
  font-size: 34px;
  padding-top: 20px;
  padding-bottom: 16px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-right: 10px;
  flex: 1;
  color: hsl(40deg 97% 54%);
  text-align: center;
}
</style>
