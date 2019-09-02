<template>
  <div class="main_container">
    <div class="logo heartBeat"></div>
    <div class="text">
      Blood Transfusion Risk During Valve Cardiac Surgery 
    </div>
    <div class="button_area center">
      <router-link to="/form">
        <el-button type="danger" round>Prediction</el-button>
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main_container {
  width: 80%;
  margin: 2em auto;
  .step_container {
    margin: 0 0 2em 0;
  }
  & > .center {
    display: flex;
    justify-content: center;
  }
  .logo {
    background-image: url('../assets/logo.png');
    background-repeat: no-repeat;
    background-size: contain;
    width: 6em;
    height: 6em;
    margin: 0 auto;
    margin-top: 6em;
  }
  
  .heartBeat {
    animation-name: heartBeat;
    animation-duration: 1.3s;
    animation-timing-function: ease-in-out;
    animation-iteration-count: infinite;
  }
  @-webkit-keyframes heartBeat {
    0% {
      transform: scale(1);
    }

    14% {
      transform: scale(1.3);
    }

    28% {
      transform: scale(1);
    }

    42% {
      transform: scale(1.3);
    }

    70% {
      transform: scale(1);
    }
  }

  @keyframes heartBeat {
    0% {
      transform: scale(1);
    }

    14% {
      transform: scale(1.3);
    }

    28% {
      transform: scale(1);
    }

    42% {
      transform: scale(1.3);
    }

    70% {
      transform: scale(1);
    }
  }
  .text {
    font-weight: bold;
    text-align: center;
  }
  .button_area {
    margin-top: 3em;
  }
}

</style>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name: 'home',
  components: {
    // HelloWorld
  },
  data() {
    return {
    }
  },
  methods: {
  }
}
</script>
