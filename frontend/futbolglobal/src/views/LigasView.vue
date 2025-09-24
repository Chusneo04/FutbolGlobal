<template>
  <div>
    <NavbarComponent></NavbarComponent>
    <h1 class="text-[50px] text-center font-bold mt-[20px]">Camisetas disponibles</h1>
    <LigasComponent></LigasComponent>
    <FooterComponent class="mt-[100px]"></FooterComponent>
  </div>
</template>

<script>
import NavbarComponent from '@/components/Navbar.vue';
import LigasComponent from '@/components/Ligas.vue';
import FooterComponent from '@/components/Footer.vue';
export default {
    name:'LigasView',
    components: {
        NavbarComponent,
        LigasComponent,
        FooterComponent
    }
}
</script>