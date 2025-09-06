<template>
  <div id="app">
    <component :is="vistaActual" />
  </div>
</template>

<script>
import InicioView from './views/InicioView.vue'

export default {
  name: 'App',
  components: {
    InicioView
  },
  computed: {
    vistaActual() {
      const path = window.location.pathname
      if (path == '/')
        return 'InicioView'
      return 'InicioView'
    }
  }
}
</script>
