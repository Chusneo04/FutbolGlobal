<template>
    <div class="flex flex-wrap w-full justify-between p-[50px] h-[110vh]">
        <CamisetaComponent v-for="(camiseta, index) in camisetas" :key="index" :id="camiseta.id" :nombre="camiseta.nombre" :stock="camiseta.stock" :precio="camiseta.precio" :imagen="camiseta.imagen"></CamisetaComponent>
    </div>
</template>

<script>
import CamisetaComponent from './Camiseta.vue';
export default {
    name: 'Camisetas_mas_vendidasComponent',
    components: {
        CamisetaComponent
    },
    data(){
        return{
            camisetas: []
        }
    },

    mounted() {
    fetch(`https://futbolglobal-frontend.onrender.com/obtener-camisetas-aleatorias`)
      .then(res => res.json())
      .then(data => {
        console.log(data);  
        this.camisetas = data;
    })
  }
}
</script>