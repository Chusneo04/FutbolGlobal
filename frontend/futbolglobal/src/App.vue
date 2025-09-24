<template>
  <div id="app" >
    <component :is="vistaActual" />
  </div>
</template>

<script>
import InicioView from './views/InicioView.vue'
import LigasView from './views/LigasView.vue'
import RegisterView from './views/RegisterView.vue'
import LoginView from './views/LoginView.vue'
import PerfilView from './views/PerfilView.vue'
export default {
  name: 'App',
  components: {
    InicioView,
    LigasView,
    RegisterView,
    LoginView,
    PerfilView
  },
  computed: {
    vistaActual() {
      const path = window.location.pathname
      if (path == '/')
        return 'InicioView'
      if (path == '/ligas')
        return 'LigasView'
      if (path == '/register')
        return 'RegisterView'
      if (path == '/login')
        return 'LoginView'
      if (path == '/perfil') {
        return 'PerfilView'
      }


      return 'InicioView'
    },
    categoriaActual(){
      const params = new URLSearchParams(window.location.search)
      return params.get('categoria')
    }
  }
}
</script>
