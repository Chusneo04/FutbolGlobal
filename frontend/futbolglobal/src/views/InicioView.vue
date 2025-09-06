<template>
  <div>
    <NavbarComponent></NavbarComponent>
    <img class="w-full h-[60vh] mt-[2rem] object-cover" src="https://static1.cdn-subsidesports.com/2/media/resized/catalog/category/600_245//media/catalog/category/mg2_teamheader_spain_2024_1.jpg"/>
  </div>
</template>

<script>
import NavbarComponent from '@/components/Navbar.vue';
export default {
  name: 'InicioView',
  components: {
    NavbarComponent
  }
}
</script>
