<template>
  <div class="w-full h-[15vh] p-[5px] px-[30px]">
    <div class="h-[80%] flex justify-between items-center">
      <div class="h-full">
        <img src="../assets/logo.png" alt="logo" class="h-full">
      </div>
      <div class="flex gap-[35px] text-[20px]">
        <p class="cursor-[pointer] bg-[#C72E22] text-[white] w-[6rem] h-[50px] flex items-center justify-center text-center rounded hover:border-[2px] hover:border-[#C72E22] hover:text-[#C72E22] hover:bg-[white] transition-colors duration-500">Perfil</p>
        <p class="cursor-[pointer] border-[2px] border-[#C72E22] text-[#C72E22] w-[6rem] flex items-center justify-center text-center rounded hover:border-none hover:bg-[#C72E22] hover:text-[white] transition-colors duration-500 delay-150">Carrito</p>
      </div>
    </div>

    <div class="w-full flex items-center justify-center gap-[50px]">
      
      <a class="text-[20px] cursor-[pointer]" href="#" @mouseenter="setActive('LaLiga')" @mouseleave="clearActive">LaLiga EA Sports</a>
      <a class="text-[20px] cursor-[pointer]" href="#" @mouseenter="setActive('Hypermotion')" @mouseleave="clearActive">LaLiga Hypermotion</a>
      <a class="text-[20px] cursor-[pointer]" href="#" @mouseenter="setActive('Otros')" @mouseleave="clearActive">Otros clubes</a>
      <a class="text-[20px] cursor-[pointer]" href="#" @mouseenter="setActive('Selecciones')" @mouseleave="clearActive">Selecciones nacionales</a>


    </div>
    <div
      v-if="active"
      class="mt-[1.5rem] h-[65vh] p-4 bg-[white] mx-[-30px] flex flex-col text-center border-[1px] rounded shadow transition-opacity duration-300 delay-150 w-screen relative"
    >
      <h1 class="text-[50px] font-bold">Camisetas {{ active }}</h1>
      <div class="flex flex-wrap w-full justify-center items-center mt-[50px]">
        <img
          v-for="(img, index) in imageMap[active]"
          :key="index"
          :src="img"
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
      imageMap: {
        LaLiga: [
          'https://assets.laliga.com/assets/2019/06/07/small/athletic.png',
          'https://assets.laliga.com/assets/2024/06/17/small/cbc5c8cc8c3e8abd0e175c00ee53b723.png',
          'https://assets.laliga.com/assets/2019/06/07/small/osasuna.png',
          'https://assets.laliga.com/assets/2025/07/11/small/0a796827f9e758d7d750db805adde7c5.png',
          'https://assets.laliga.com/assets/2020/09/01/small/27002754a98bf535807fe49a24cc63ea.png',
          'https://assets.laliga.com/assets/2019/06/07/small/elche.png',
          'https://assets.laliga.com/assets/2019/06/07/small/barcelona.png',
          'https://assets.laliga.com/assets/2023/05/12/small/dc59645c96bc2c9010341c16dd6d4bfa.png',
          'https://assets.laliga.com/assets/2022/06/22/small/8f43addbb29e4a72f5e90b6edfe4728f.png',
          'https://assets.laliga.com/assets/2019/06/07/small/levante.png',
          'https://assets.laliga.com/assets/2023/04/27/small/57d9950a8745ead226c04d37235c0786.png',
          'https://assets.laliga.com/assets/2025/07/02/small/e9177f6edd72c6360602adbca85e442f.png',
          'https://assets.laliga.com/assets/2023/03/22/small/013ae97735bc8e519dcf30f6826168ca.png',
          'https://assets.laliga.com/assets/2022/09/15/small/e4a09419d3bd115b8f3dab73d480e146.png',
          'https://assets.laliga.com/assets/2019/06/07/small/real-madrid.png',
          'https://assets.laliga.com/assets/2019/06/07/small/oviedo.png',
          'https://assets.laliga.com/assets/2019/06/07/small/real-sociedad.png',
          'https://assets.laliga.com/assets/2019/06/07/small/sevilla.png',
          'https://assets.laliga.com/assets/2019/06/07/small/valencia.png',
          'https://assets.laliga.com/assets/2019/06/07/small/villarreal.png'
        ],
        Hypermotion: [
          'https://assets.laliga.com/assets/2019/11/18/small/dff48b7d706547a0c406464cb1ee9218.png',
          'https://assets.laliga.com/assets/2019/06/07/small/albacete.png',
          'https://assets.laliga.com/assets/2021/06/24/small/8de24d38ab1472bbae1620d36582d7bd.png',
          'https://assets.laliga.com/assets/2019/06/07/small/cadiz.png',
          'https://assets.laliga.com/assets/2019/11/18/small/0cb9fb4e471b8fe16fe9f6f193188505.png',
          'https://assets.laliga.com/assets/2019/06/07/small/leganes.png',
          'https://assets.laliga.com/assets/2019/06/07/small/mirandes.png',
          'https://assets.laliga.com/assets/2019/06/07/small/cordoba.png',
          'https://assets.laliga.com/assets/2025/06/30/small/53a29bba024e311db4aea85228c8aa12.png',
          'https://assets.laliga.com/assets/2022/06/17/small/33215c0212bcad95cc5d67b2b5a33fb8.png',
          'https://assets.laliga.com/assets/2023/01/17/small/f5db12f3a29fdfd14a0d50337016dc95.png',
          'https://assets.laliga.com/assets/2019/06/07/small/malaga.png',
          'https://assets.laliga.com/assets/2019/06/07/small/racing.png',
          'https://assets.laliga.com/assets/2019/06/07/small/real-sociedad.png',
          'https://assets.laliga.com/assets/2019/06/07/small/deportivo.png',
          'https://assets.laliga.com/assets/2019/06/07/small/sporting.png',
          'https://assets.laliga.com/assets/2024/06/17/small/1467dcd5efb813a742d86f8eb39504a3.png',
          'https://assets.laliga.com/assets/2019/06/07/small/zaragoza.png',
          'https://assets.laliga.com/assets/2019/06/07/small/eibar.png',
          'https://assets.laliga.com/assets/2023/07/10/small/33fab7067fb4c797cfb5ce179a045b64.png',
          'https://assets.laliga.com/assets/2019/06/07/small/almeria.png',
          'https://assets.laliga.com/assets/2019/06/07/small/las-palmas.png'
        ],
        Otros: [
          'https://img.legaseriea.it/vimages/62cef513/milan.png?webp&q=70&size=-x319.5',
          'https://resources.premierleague.com/premierleague25/badges-alt/3.svg',
          'https://img.legaseriea.it/vimages/62cfd69d/atalanta.png?webp&q=70&size=300x-',
          'https://www.bundesliga.com/assets/clublogo/DFL-CLU-00000B.svg',
          'https://brasileirao-cbf.s3.amazonaws.com/img/times/botafogo.png',
          'https://www.ligaprofesional.ar/wp-content/uploads/2024/06/BOC-escudo.png',
          'https://www.ligaprofesional.ar/wp-content/uploads/2024/06/RIV-escudo.png',
          'https://resources.premierleague.com/premierleague25/badges-alt/8.svg',
          'https://brasileirao-cbf.s3.amazonaws.com/img/times/atletico-mineiro.png',
          'https://statics-maker.llt-services.com/prl/images/2023/06/22/xlarge/2fe3ad4a-c545-4ed7-b4d7-dedf4b4f5547.png',
          'https://brasileirao-cbf.s3.amazonaws.com/img/times/flamengo.png',
          'https://www.bundesliga.com/assets/clublogo/DFL-CLU-00000G.svg',
          'https://img.legaseriea.it/vimages/62cef496/inter.png?webp&q=70&size=300x-',
          'https://www.futbox.com/img/v1/17f/326/4c8/ae2/3499c8f58b17fa84cc38_zoom.png',
          'https://logodownload.org/wp-content/uploads/2017/02/liverpool-fc-logo-escudo.png',
          'https://resources.premierleague.com/premierleague25/badges-alt/43.svg',
          'https://s3.eu-west-1.amazonaws.com/image.mpg/assets/clubs/logo/2023_1_13_512x512_4a9438034a011c1368c52d097a93b98f.png',
          'https://media.slbenfica.pt/-/media/images/slb-logo-new.svg?v=638097287260000000',
          'https://img.legaseriea.it/vimages/62cef4d5/lazio.png?webp&q=70&size=300x-',
          'https://www.bundesliga.com/assets/clublogo/DFL-CLU-000007.svg'

        ],
        Selecciones: [
          'https://logodownload.org/wp-content/uploads/2016/11/argentina-national-football-team-logo-0-1.png',
          'https://upload.wikimedia.org/wikipedia/commons/6/6a/Escudo_selecci%C3%B3n_espa%C3%B1ola.png',
          'https://logodownload.org/wp-content/uploads/2022/07/france-national-football-team-logo-1.png',
          'https://www.futbox.com/img/v1/963/97d/2e8/462/01fea69e0291a0c27481_zoom.png',
          'https://logodownload.org/wp-content/uploads/2022/12/brazil-national-football-team-logo-1.png',
          'https://logodownload.org/wp-content/uploads/2021/10/fpf-selecao-de-portugal-logo-1.png',
          'https://logodownload.org/wp-content/uploads/2022/07/holanda-netherlands-football-team-logo.png',
          'https://logodownload.org/wp-content/uploads/2022/09/belgian-national-team-logo-1.png',
          'https://logodownload.org/wp-content/uploads/2018/06/germany-national-football-team-logo.png',
          'https://logodownload.org/wp-content/uploads/2022/11/croatia-national-football-team-logo.png',
          'https://logodownload.org/wp-content/uploads/2023/08/italy-national-football-team-logo-0.png',
          'https://upload.wikimedia.org/wikipedia/commons/b/bd/Morocco_FRMF.png',
          'https://logodownload.org/wp-content/uploads/2021/10/fmf-seleccion-de-mexico-logo-5.png',
          'https://upload.wikimedia.org/wikipedia/commons/f/f0/Escudo_de_la_Federaci%C3%B3n_Colombiana_de_F%C3%BAtbol.png',
          'https://logodownload.org/wp-content/uploads/2021/10/united-states-national-soccer-team-logo-1.png',
          'https://logodownload.org/wp-content/uploads/2021/09/auf-seleccion-de-futbol-de-uruguay-logo-1.png',
          'https://logodownload.org/wp-content/uploads/2022/08/japan-national-football-team-logo.png',
          'https://logodownload.org/wp-content/uploads/2022/07/fsf-senegal-national-football-team-logo.png',
          'https://logodownload.org/wp-content/uploads/2022/11/switzerland-national-football-team-logo.png',
          'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxlVfD8ygU1sppoG3TuIec-Te1vwMA2Zpw-g&s'

        ],
      },
    }
  },
  methods: {
    setActive(key) {
      this.active = key
    },
    clearActive() {
      this.active = null
    },
  },
}
</script>

