<template>
    <div>
        <NavbarLogueadoComponent></NavbarLogueadoComponent>
        <div class="mt-[50px] w-full flex flex-col items-center justify-center">
            <h1 class="text-[50px] font-bold text-[#C72E22] text-center">Tu carrito</h1>
            <table class="w-[80%] flex flex-col">
                <thead class="rounded-t-[20px]">
                    <tr class="w-full flex flex-row justify-between h-[50px] text-[20px] bg-[#C72E22] text-[white] rounded-t-[20px]">
                        <th class="w-[50%] text-center flex items-center justify-center">Imagen</th>
                        <th class="w-full text-center flex items-center justify-center">Nombre</th>
                        <th class="w-[25rem] text-center flex items-center justify-center">Precio unidad</th>
                        <th class="w-[20rem] text-center flex items-center justify-center">Cantidad</th>
                        <th class="w-[20rem] text-center flex items-center justify-center">Precio total</th>
                        <th class="w-[20rem] text-center flex items-center justify-center">Acciones</th>
                    </tr>
                </thead>
                <tbody class="flex flex-col gap-[20px] bg-[lightgray]">
                    <tr v-for="(elemento, index) in carrito" :key="index" class=" w-full flex flex-row justify-between h-[100px] text-[black] mt-[10px] mb-[10px]">      
                        <td class="flex items-center justify-center w-[50%]"><img :src="elemento.imagen " class="h-full "/></td>
                        <td class="flex items-center justify-center w-full text-center text-[25px]"><h1>{{ elemento.nombre }}</h1></td>
                        <td class="flex items-center justify-center w-[25rem] text-center text-[25px]"><p>{{ elemento.precio }}€</p></td>
                        <td class="flex items-center justify-center w-[20rem] text-center text-[25px]"><p>{{ elemento.cantidad }}</p></td>
                        <td class="flex items-center justify-center w-[20rem] text-center text-[25px]"><p>{{ elemento.cantidad * elemento.precio }}€</p></td>
                        <td class="flex items-center justify-center w-[20rem] text-center text-[25px] text-[#C72E22]"><button @click="eliminarCarrito(elemento.nombre)" class="w-full cursor-pointer"><i class="fa-solid fa-trash"></i></button></td>
                    </tr>
                </tbody>
            </table>

            <button @click="comprar()" class="cursor-[pointer] bg-[#C72E22] mt-[50px] mb-[50px] text-[white] w-[10rem] h-[50px] flex items-center justify-center text-center rounded hover:border-[2px] hover:border-[#C72E22] hover:text-[#C72E22] hover:bg-[white] transition-colors duration-500">Finalizar compra</button>


        </div>
        <FooterComponent></FooterComponent>
    </div>
  
</template>

<script>
import NavbarLogueadoComponent from '@/components/NavbarLogueado.vue'
import FooterComponent from '@/components/Footer.vue'
export default {
    name: 'CarritoView',
    components:{
        NavbarLogueadoComponent,
        FooterComponent
    },
    data(){
        return {
            carrito:[]
        }
    },
    methods:{
        obtenerCarrito(){
            const correo = this.$cookies.get('usuario')
            fetch(`http://localhost:5000/obtener_carrito/${correo}`)
                .then(res => res.json())
                .then(data => {
                    console.log(data);
                    if (data.length === 0) {
                        window.location.href = '/perfil'
                        alert('No tienes productos en el carrito')
                        
                    }else{
                        this.carrito = data
                    }
                    
                })
        },
        eliminarCarrito(nombre){
            fetch('http://localhost:5000/eliminar_carrito', {
                method : 'DELETE',
                headers: {
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({'nombre':nombre})
            })
            .then(res => res.json())
            .then(data => {
                alert(data.mensaje)
                this.obtenerCarrito()
            })
            
        },
        comprar(){
            const correo = this.$cookies.get('usuario')
            fetch('http://localhost:5000/comprar', {
                method: 'DELETE',
                headers:{
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({'correo':correo})
            })
            .then(res => res.json())
            .then(data => {
                alert(data.mensaje)
            })
        }
    },
    mounted(){
        this.obtenerCarrito()
    }

}
</script>
