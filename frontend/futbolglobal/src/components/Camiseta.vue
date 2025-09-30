<template>
  <div class="border-[1px] w-[50vh] h-[90vh] rounded-[50px]">
    <img class="w-full h-[60%] rounded-t-[50px]" :src="imagen" alt="Imagen camiseta"/>

    <div class="h-full m-[10px] flex flex-col items-center gap-[25px]">
        <h1 class="text-center text-[18px] font-semibold h-[30px]">{{ nombre }}</h1>
        <p class="text-[25px] font-bold">{{ precio }}€</p>
        <div class="flex flex-row items-center justify-center gap-[50px]  text-[30px] h-[30px]">
            <button @click="restar" class="hover:bg-[#E33432] p-[10px] w-[50px] text-center">-</button>
            <p>{{ cantidad }}</p>
            <button @click="sumar" class="hover:bg-[#2EBF35] p-[10px] w-[50px] text-center">+</button>
        </div>
        <button @click="añadir()" class="cursor-[pointer] bg-[#C72E22] text-[white] w-[9rem] h-[50px] flex items-center justify-center text-center rounded hover:border-[2px] hover:border-[#C72E22] hover:text-[#C72E22] hover:bg-[white] transition-colors duration-500">Añadir al carrito</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'CamisetaComponent',
    props: {
        imagen: String,
        nombre: String,
        precio: Number,
        id: Number,
        stock: Number
    },
    data(){
        return {
            cantidad: 0
        }
    },
    methods: {
        sumar(){
            if (this.cantidad < this.stock) {
                this.cantidad ++
            }
            
            
        },
        restar(){
            if (this.cantidad > 0) {
                this.cantidad --
            }
        },
        async añadir(){
            const cookie = this.$cookies.get('usuario')
            if (!cookie){
                alert('Debes estar autenticado para añadir al carrito')
            }
            else{
                const datos = {
                    imagen : this.imagen,
                    nombre : this.nombre,
                    precio : this.precio,
                    cantidad : this.cantidad,
                    cookie : cookie
                }
                const respuesta = await fetch(`https://futbolglobal-frontend.onrender.com/añadir_carrito/${this.id}`,{
                    method : 'POST',
                    headers : {
                        'Content-Type':'application/json'
                    },
                    body : JSON.stringify(datos) 
                })
                const resultado = await respuesta.json(respuesta)
                alert(resultado.mensaje)
            }
        }
    }
}
</script>

