<template>
  <div>
    <NavbarComponent></NavbarComponent>
    <img class="w-full h-[60vh] mt-[2rem] object-cover" src="https://static1.cdn-subsidesports.com/2/media/resized/catalog/category/600_245//media/catalog/category/mg2_teamheader_spain_2024_1.jpg"/>
    <h1 class="text-center text-[50px] mt-[20px] font-semibold">Nuestras camisetas mas vendidas</h1>
    <Camisetas_mas_vendidasComponent></Camisetas_mas_vendidasComponent>
  </div>
</template>

<script>
import NavbarComponent from '@/components/Navbar.vue';
import Camisetas_mas_vendidasComponent from '@/components/Camisetas_mas_vendidas.vue';
export default {
  name: 'InicioView',
  components: {
    NavbarComponent,
    Camisetas_mas_vendidasComponent
  }
}
</script>
