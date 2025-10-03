<template>
  <div>
    <div class="h-[15vh] flex justify-between items-center bg-[white] w-full px-[20px]">
      <div class="h-full">
        <a href="/" class="flex items-center justify-center h-full"><img src="../assets/logo.png" alt="logo" class="h-[70%] "></a>
      </div>
      <div class="flex gap-[35px] text-[20px]">
        <p class="cursor-[pointer] border-[2px] border-[#C72E22] text-[#C72E22] w-[6rem] h-[50px] flex items-center justify-center text-center rounded hover:border-none hover:bg-[#C72E22] hover:text-[white] transition-colors duration-500 delay-150">Carrito</p>
      </div>
    </div>
    <div class="w-full flex flex-col justify-center items-center bg-[#C72E22] py-[30px]">
        <div class="border-[1px] h-[30rem] w-[40rem] mt-[10vh] bg-[white] p-[10px] rounded-[30px]">
            <h1 class="text-[#C72E22] text-[50px] font-bold text-center">Registro</h1>
            <form @submit.prevent = registrarUsuario  class="flex flex-col items-center justify-center gap-[30px] w-full p-[10px]">
                <input type="text" name="nombre" id="nombre" placeholder="Nombre" v-model="nombre" required class="h-[50px] w-[80%] p-[10px] border-[black] border-[2px] rounded-[10px] outline-none">
                <input type="email" name="correo" id="correo" placeholder="Correo Electrónico" v-model="correo" required class="w-[80%] h-[50px] p-[10px] border-[black] border-[2px] rounded-[10px] outline-none">
                <input type="password" name="clave" id="clave" placeholder="Contraseña" v-model="clave" required class="w-[80%] h-[50px] p-[10px] border-[black] border-[2px] rounded-[10px] outline-none">
                <p class="text-[#C72E22]">¿Quieres iniciar sesión? <a href="/login" class="underline">Iniciar Sesión</a></p>
                <button type="submit" class="bg-[#C72E22] w-[35%] h-[50px] rounded-[20px] text-[20px] text-[white] cursor-[pointer] hover:border-[2px] hover:border-[#C72E22] hover:text-[#C72E22] hover:bg-[white] transition-colors duration-500 delay-150">Registrar Usuario</button>
            </form>
        </div>
    </div>
    <FooterComponent></FooterComponent>
  </div>  
  
</template>

<script>
import FooterComponent from '@/components/Footer.vue';
export default {
    name: 'RegisterView',
    data() {
        return {
            nombre: '',
            correo: '',
            clave: ''
        }
    },
    components:{
        FooterComponent
    },
    methods: {
        async registrarUsuario(){
            const datos = {
                nombre: this.nombre,
                correo: this.correo,
                clave: this.clave
            }
            const respuesta = await fetch('http://localhost:5000/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            })
            const resultado = await respuesta.json()
            window.location.href = '/perfil'
            
            alert(resultado.mensaje);
            
        },
        usuario_logueado(){
            const usuario_logueado = this.$cookies.get('usuario')
            if (usuario_logueado) {
                window.location.href = '/perfil'
            }
            
        }
    },
    mounted(){
        this.usuario_logueado()
    }
}
</script>