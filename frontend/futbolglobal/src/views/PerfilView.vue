<template>
    <div>
        <NavbarLogueadoComponent></NavbarLogueadoComponent>
        <a @click="cerrarSesion()" class="ml-[20px] cursor-[pointer] border-[2px] border-[#C72E22] text-[#C72E22] w-[8rem] flex items-center justify-center text-center rounded hover:bg-[#C72E22] hover:text-[white] transition-colors duration-500 delay-150">Cerrar Sesion</a>
        <div class="mt-[50px] w-full flex flex-col items-center justify-center">
            <h1 class="text-[50px] font-bold text-[#C72E22]">Bienvenido a tu perfil, {{ usuario.nombre }}, aqui tienes tus pedidos</h1>
        
            <table class="w-[80%] flex flex-col mt-[50px] mb-[50px]">
                <thead class="rounded-t-[20px]">
                    <tr class="w-full flex flex-row justify-between h-[50px] text-[20px] bg-[#C72E22] text-[white] rounded-t-[20px]">
                        <th class="w-[50%] text-center flex items-center justify-center">Imagen</th>
                        <th class="w-full text-center flex items-center justify-center">Nombre</th>
                        <th class="w-[25rem] text-center flex items-center justify-center">Precio unidad</th>
                        <th class="w-[20rem] text-center flex items-center justify-center">Cantidad</th>
                        <th class="w-[20rem] text-center flex items-center justify-center">Precio total</th>
                    </tr>
                </thead>
                <tbody class="flex flex-col gap-[20px] bg-[lightgray]">
                    <tr v-for="(elemento, index) in pedidos" :key="index" class=" w-full flex flex-row justify-between h-[100px] text-[black] mt-[10px] mb-[10px]">      
                        <td class="flex items-center justify-center w-[50%]"><img :src="elemento.imagen " class="h-full "/></td>
                        <td class="flex items-center justify-center w-full text-center text-[25px]"><h1>{{ elemento.nombre }}</h1></td>
                        <td class="flex items-center justify-center w-[25rem] text-center text-[25px]"><p>{{ elemento.precio }}€</p></td>
                        <td class="flex items-center justify-center w-[20rem] text-center text-[25px]"><p>{{ elemento.cantidad }}</p></td>
                        <td class="flex items-center justify-center w-[20rem] text-center text-[25px]"><p>{{ elemento.cantidad * elemento.precio }}€</p></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <FooterComponent></FooterComponent>
    </div>
</template>

<script>
import NavbarLogueadoComponent from '@/components/NavbarLogueado.vue';
import FooterComponent from '@/components/Footer.vue'
export default {
    name: 'PerfilView',
    components: {
        NavbarLogueadoComponent,
        FooterComponent
    },
    data(){
        return{
            usuario: '',
            pedidos:[]
        }
        
    },
    methods: {
        async cerrarSesion(){
            const respuesta = await fetch('http://localhost:5000/logout',{
                method: 'POST',
                credentials: 'include'
            })
            const resultado = await respuesta.json()
            alert(resultado.mensaje)
            window.location.href = '/'
        },
        obtenerUsuario(){
            const correo = this.$cookies.get('usuario')
            fetch(`http://localhost:5000/obtener-usuario/${correo}`)
                .then(res => res.json())
                .then(data => {
                    this.usuario = data
                    console.log(data);
                    
                })
                .catch(err => {
                    alert('Error al cargar el usuario', err)
                })
            
        },
        usuario_logueado(){
            const usuario_logueado = this.$cookies.get('usuario')
            if (!usuario_logueado) {
                window.location.href = '/login'
            }
            else{
                this.obtenerUsuario(),
                this.obtenerPedidos()
            }
            
        },
        obtenerPedidos(){
            const correo = this.$cookies.get('usuario')
            fetch(`http://localhost:5000/obtener_pedidos/${correo}`)
                .then(res => res.json())
                .then(data => {
                    console.log(data);
                    if (data.length === 0) {
                        window.location.href = '/'
                        alert('No tienes pedidos')
                        
                    }else{
                        this.pedidos = data
                    }
                })
        }
        
    },
    mounted(){
        this.usuario_logueado()
    }
}
</script>