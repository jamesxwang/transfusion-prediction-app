<template>
  <div class="prediction">
    <h1 v-if="predictionResult != -1">Result: {{ predictionResult }}</h1>
    <h1 v-else>This is the prediction page</h1>
  </div>
</template>

<script>
export default {
  name: 'prediction',
  data() {
    return {
      predictionResult: -1
    }
  },
  watch: {
    'this.$route.params.result': function(val) {
      if (val == 1)
        this.predictionResult = true;
      else if (val == 0)
        this.predictionResult = false;
    }
  }
}
</script>