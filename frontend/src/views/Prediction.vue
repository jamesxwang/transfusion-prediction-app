<template>
  <div class="prediction">
    <div v-if="predictionResult === 0 || predictionResult === 1">
      <h1>{{ computedResult }}</h1>
      <p>The probability is {{ computedPredictionProb }} %</p>
      <el-divider></el-divider>
      <div v-if="false">
        <el-switch v-model="showAll" active-text="Show More" inactive-text="Show Results-Realated"></el-switch>
        <el-divider></el-divider>
      </div>
      <div id="chart">
        <apexchart
          v-if="showAll"
          type="bar"
          height="500"
          :options="chartOptions"
          :series="chartOptions.series"
        />
        <apexchart
          v-else
          type="bar"
          height="350"
          :options="chartOptionsRR"
          :series="chartOptionsRR.series"
        />
      </div>
    </div>
    <!-- <button @click="updateChart">Update</button> -->
    <!-- v-else -->
    <h1 v-else>This is the prediction page</h1>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import translation from "../locale/translate";

export default {
  name: "prediction",
  components: {
    apexchart: VueApexCharts
  },
  methods: {
    translate(chinese) {
      return translation[chinese];
    },
    updateChart() {
      const data = [...this.rawData.positive, ...this.rawData.negative]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5);
      const categories = data.map(d => this.translate(d[0]));
      const series = data.map(d => (d[1] * 100).toFixed(2));
      const colors = this.predictionResult === 1 ? ["#FF4560"] : ["#008FFB"];
      this.chartOptionsRR = {
        ...this.chartOptionsRR,
        ...{
          colors: colors,
          series: [
            {
              name: "Impact Rate",
              data: series
            }
          ],
          xaxis: {
            categories: this.predictionResult === 1 ? categories : categories
          }
        }
      };

      // legacy
      this.chartOptions = {
        ...this.chartOptions,
        ...{
          series: [
            {
              name: "Positive",
              data: this.positiveChartData
            },
            {
              name: "Negative",
              data: this.negativeChartData
            }
          ],
          xaxis: {
            categories: this.categories
          }
        }
      };
    }
  },
  data() {
    return {
      predictionResult: "",
      rawData: null,
      showAll: false,
      negativeChartData: [],
      positiveChartData: [],
      categories: [],
      chartOptionsRR: {
        plotOptions: {
          bar: {
            horizontal: true
          }
        },
        title: {
          text: "Transfusion Prediction Relevance Chart"
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 1,
          colors: ["#fff"]
        },
        tooltip: {
          shared: false,
          y: {
            formatter: function(val) {
              return Math.abs(val) + "%";
            }
          }
        }
      },
      chartOptions: {
        chart: {
          stacked: true
        },
        colors: ["#008FFB", "#FF4560"],
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: "80%"
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 1,
          colors: ["#fff"]
        },
        grid: {
          xaxis: {
            showLines: false
          }
        },
        yaxis: {
          title: {
            text: "Percentage"
          }
        },
        tooltip: {
          shared: false,
          x: {
            formatter: function(val) {
              return val;
            }
          },
          y: {
            formatter: function(val) {
              return Math.abs(val) + "%";
            }
          }
        },
        title: {
          text: "Transfusion Prediction Relevance Chart"
        },
        xaxis: {
          categories: [],
          labels: {
            formatter: function(val) {
              return Math.abs(Math.round(val)) + "%";
            }
          }
        }
      }
    };
  },
  computed: {
    computedResult: function() {
      if (this.predictionResult === 0) {
        return "Result: No need for blood transfusion.";
      } else if (this.predictionResult === 1) {
        return "Result: Blood Transfusion needed.";
      } else {
        return "";
      }
    },
    computedPredictionProb: function() {
      return (this.predictionProb * 100).toFixed(2);
    }
  },
  watch: {
    "$route.params": {
      handler: function(val) {
        if (
          val &&
          val.negativeChartData &&
          val.positiveChartData &&
          val.categories
        ) {
          this.rawData = val.rawData;
          this.predictionResult = val.result;
          this.predictionProb = val.prob;
          this.negativeChartData = val.negativeChartData;
          this.positiveChartData = val.positiveChartData;
          this.categories = val.categories;
          this.updateChart();
        }
      },
      deep: true,
      immediate: true
    }
  }
};
</script>