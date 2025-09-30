<template>
  <div class="w-full h-[15vh] p-[5px] px-[30px]">
    <div class="h-[80%] flex justify-between items-center">
      <div class="h-full">
        <a href="/"><img src="../assets/logo.png" alt="logo" class="h-full"></a>
      </div>
      <div class="flex gap-[35px] text-[20px]">
        <a href="/perfil" class="cursor-[pointer] bg-[#C72E22] text-[white] w-[6rem] h-[50px] flex items-center justify-center text-center rounded hover:border-[2px] hover:border-[#C72E22] hover:text-[#C72E22] hover:bg-[white] transition-colors duration-500">Perfil</a>
        <a href="/carrito" class="cursor-[pointer] border-[2px] border-[#C72E22] text-[#C72E22] w-[6rem] flex items-center justify-center text-center rounded hover:border-none hover:bg-[#C72E22] hover:text-[white] transition-colors duration-500 delay-150">Carrito</a>
      </div>
    </div>

    <div class="w-full flex items-center justify-center gap-[50px]">
      
      <a class="text-[20px] cursor-[pointer]" href="/ligas?categoria=LaLiga" @mouseenter="setActive('LaLiga')" @mouseleave="clearActive">LaLiga EA Sports</a>
      <a class="text-[20px] cursor-[pointer]" href="/ligas?categoria=Hypermotion" @mouseenter="setActive('Hypermotion')" @mouseleave="clearActive">LaLiga Hypermotion</a>
      <a class="text-[20px] cursor-[pointer]" href="/ligas?categoria=Otros" @mouseenter="setActive('Otros')" @mouseleave="clearActive">Otros clubes</a>
      <a class="text-[20px] cursor-[pointer]" href="/ligas?categoria=Selecciones" @mouseenter="setActive('Selecciones')" @mouseleave="clearActive">Selecciones nacionales</a>


    </div>
    <div
      v-if="active"
      class="mt-[1.5rem] h-[65vh] p-4 bg-[white] mx-[-30px] flex flex-col text-center border-[1px] rounded shadow  w-screen relative"
    >
      <h1 class="text-[50px] font-bold">Camisetas {{ active }}</h1>
      <div class="flex flex-wrap w-full justify-center items-center mt-[50px]">
        <img
          v-for="(equipo, index) in datos"
          :key="index"
          :src="equipo.imagen"
          alt="Imagen relacionada"
          class="w-[8rem] h-[8rem] rounded p-[5px]"
        />
      </div>
      
    </div>

  </div>
</template>

<script>
export default {
  name: 'NavbarComponent',
  data() {
    return {
      active: null,
      datos:[]
    }
  },
  methods: {
    setActive(key) {
      this.active = key;
      
      fetch(`http://localhost:5000/obtener_equipos/${key}`)
      .then(res => res.json())
      .then(data => {
        console.log(data);  
        this.datos = data;
      })
    },
    clearActive() {
      this.active = null
    },
  }
}
</script>

