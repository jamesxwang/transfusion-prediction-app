<template>
  <div class="prediction">
    <h1 v-if="this.$route.params.result">Result: {{ this.$route.params.result || 'Null' }}</h1>
    <h1 v-else>This is the prediction page</h1>
  </div>
</template>
