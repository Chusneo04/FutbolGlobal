<template>
  <div class="border-[1px] w-[50vh] h-[80vh] rounded-[50px]">
    <img class="w-full h-[60%] rounded-t-[50px]" src="" alt="Imagen camiseta"/>
    <div class="h-full m-[10px] flex flex-col items-center gap-[20px]">
        <h1 class="text-center text-[18px] font-semibold">Primera equipación Real Madrid 25-26</h1>
        <p class="text-[25px] font-bold">120€</p>
        <div class="flex flex-row items-center justify-center gap-[50px]  text-[30px] ">
            <button @click="restar" class="hover:bg-[#E33432] p-[10px] w-[50px] text-center">-</button>
            <p>{{ cantidad }}</p>
            <button @click="sumar" class="hover:bg-[#2EBF35] p-[10px] w-[50px] text-center">+</button>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'CamisetaComponent',
    data(){
        return {
            cantidad: 0
        }
    },
    methods: {
        sumar(){
            this.cantidad ++
        },
        restar(){
            if (this.cantidad > 0) {
                this.cantidad --
            }
        }
    }
}
</script>

