<template>
  <div class="flex flex-wrap w-full justify-center items-center p-[50px] gap-x-[100px] gap-y-[100px]">
    <CamisetaComponent v-for="(camiseta, index) in camisetas" :key="index" :id="camiseta.id" :nombre="camiseta.nombre" :stock="camiseta.stock" :precio="camiseta.precio" :imagen="camiseta.imagen"></CamisetaComponent>
  
  </div>
</template>

<script>
import CamisetaComponent from './Camiseta.vue';
export default {
  name: 'LigasComponent',
  components: {
    CamisetaComponent
  },
  data() {
    return {
      camisetas: [],
      categoria: null
    }
  },
  methods: {
    cargarLigas(categoria) {
      fetch(`https://futbolglobal-frontend.onrender.com/obtener-camisetas/${encodeURIComponent(categoria)}`)
        .then(res => res.json())
        .then(data => {
          console.log(data)
          this.camisetas = data
        })
        .catch(err => {
          console.error('Error al cargar camisetas:', err)
        })
    }
  },
  mounted() {
    const params = new URLSearchParams(window.location.search)
    this.categoria = params.get('categoria') || 'todas'
    this.cargarLigas(this.categoria)
  }
}
</script>
