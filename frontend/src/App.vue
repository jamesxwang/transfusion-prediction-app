<template>
  <div id="app">
    <el-container class="main"> 
      <el-header>
        <router-link to="/">
          <div id="logo"></div>
        </router-link>     
        <div class="nav_text">Transfusion Prediction</div>
      </el-header>
      <el-main>
        <router-view/>
      </el-main>
      <!-- <el-footer>Footer</el-footer> -->
    </el-container>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}
#logo {
  background-image: url('assets/logo.png');
  background-repeat: no-repeat;
  background-size: contain;
  width: 2em;
  height: 2em;
  float: left;
  margin: 1em auto;
}
.nav_text {
  color: #fff;
  text-align: center;
  overflow: hidden;
  font-size: large;
  margin: 1em auto;
  // vertical-align: middle;
}
.el-header {
  background-color: #303133;
  z-index: 100;
}
.main {
  height: 100vh;
}
// div{
//   margin: 20px auto;
// }
</style>
