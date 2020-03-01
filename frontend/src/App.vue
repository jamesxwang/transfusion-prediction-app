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
      <el-footer class="footer">
        <el-row :gutter="20">
          <el-col  :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
            <address>
              Copyright ©
              <a href="http://transfusionprediction.cn/">transfusionprediction.cn</a>
              All Rights Reserved
            </address>
          </el-col>
          <el-col  :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
            <address class="beian">
              <a href="http://www.beian.gov.cn" target="_blank">湘ICP备19019235号</a>
            </address>
          </el-col>
        </el-row>
      </el-footer>
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
@media only screen and (max-width: 768px) {
  .footer {
    text-align: center;
  }
}
@media only screen and (min-width: 769px) {
  .beian {
    float: right;
    text-decoration: none;
  }
}
// div{
//   margin: 20px auto;
// }
</style>
