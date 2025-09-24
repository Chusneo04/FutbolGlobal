<template>
    <div>
        <NavbarLogueadoComponent></NavbarLogueadoComponent>
        <a @click="cerrarSesion()" class="ml-[20px] cursor-[pointer] border-[2px] border-[#C72E22] text-[#C72E22] w-[8rem] flex items-center justify-center text-center rounded hover:bg-[#C72E22] hover:text-[white] transition-colors duration-500 delay-150">Cerrar Sesion</a>
        <div class="w-full text-center">
            <h1 class="text-[50px] font-bold text-[#C72E22]">Bienvenido a tu perfil, {{ usuario.nombre }}</h1>
        </div>
    </div>
</template>

<script>
import NavbarLogueadoComponent from '@/components/NavbarLogueado.vue';
export default {
    name: 'PerfilView',
    components: {
        NavbarLogueadoComponent
    },
    data(){
        return{
            usuario: ''
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
                this.obtenerUsuario()
            }
            
        }
        
    },
    mounted(){
        this.usuario_logueado()
    }
}
</script>