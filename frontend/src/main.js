import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
Vue.use(ElementUI, { locale })

Vue.config.productionTip = false
axios.defaults.timeout = 5000
axios.interceptors.response.use(response => {
	return response
})

axios.interceptors.request.use(config => {
	config.headers = {
	  'Content-Type':'application/json'
	}
	return config
},err => {
	return Promise.reject(err)
})

Vue.prototype.$axios = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
