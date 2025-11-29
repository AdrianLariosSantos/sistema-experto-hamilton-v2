<template>
  <div>
    <section class="mb-20">
      <div class="block md:flex md:space-x-10">
        <div class="w-full md:w-1/2 flex flex-col justify-center">
          <div class="flex flex-col border-b-2 border-gray-100 pb-8">
            <div class="relative mb-5">
              <span
                class="
                  rounded-lg
                  inline-flex
                  p-3
                  ring-4 ring-white
                  text-maincolor-700
                  bg-maincolor-50
                "
              >
                <hero-icon
                  icon="IdentificationIcon"
                  class="h-6 w-6"
                ></hero-icon>
              </span>
            </div>
            <p class="text-3xl font-extrabold mb-5">
              Actualizacion de datos de contacto
            </p>
            <span class="text-gray-500 text-justify">
              Proyecto de Acuerdo 00/2022 por el que se instruye a los
              integrantes de la Policía de proximidad a señalar un domicilio
              para oir y recibir notificaciones y documentos en la Ciudad de
              México, asi como mantenerlo actualizado.
            </span>
            <span class="text-gray-500 mb-5 mt-2 text-justify text-xs italic">
              De conformidad con el articulo 59, fraccion XXXII, de la ley del
              sistema de seguridad ciudadana de la Ciudad de México
            </span>
            <div>
              <i-button
                variant="maincolor"
                size="lg"
                :to="{ name: 'acuerdoNotificaciones' }"
                >Iniciar registro</i-button
              >
            </div>
          </div>
        </div>
        <div class="hidden md:block md:w-1/2 md:px-10">
          <img
            src="https://via.placeholder.com/300"
            class="w-full h-auto mx-auto shadow-lg rounded-lg"
          />
        </div>
      </div>
    </section>
    <!-- <section
      class="bg-maincolor-50 py-5"
      style="margin-left: -100rem; margin-right: -100rem"
    >
      <div class="py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="lg:text-center">
            <h2
              class="
                text-base text-verdebienestar-600
                font-semibold
                tracking-wide
                uppercase
              "
            >
              MI PERFIL
            </h2>
            <p
              class="
                mt-2
                text-3xl
                leading-8
                font-extrabold
                tracking-tight
                text-gray-900
                sm:text-4xl
              "
            >
              Tu cuenta Mi Perfil te da acceso a
            </p>
            <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
              Programas, Convocatorias y Beneficios exclusivos para ti, integrante de la Secretaría de Seguridad Ciudadana de la Ciudad de México.
            </p>
          </div>

          <div class="mt-10">
            <dl
              class="
                space-y-10
                md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10
              "
            >
              <div
                v-for="feature in features"
                :key="feature.name"
                class="relative"
              >
                <dt>
                  <div
                    class="
                      absolute
                      flex
                      items-center
                      justify-center
                      h-12
                      w-12
                      rounded-md
                      bg-verdebienestar-500
                      text-white
                    "
                  >
                    <hero-icon :icon="feature.icon" class="h-6 w-6"/>
                  </div>
                  <p class="ml-16 text-lg leading-6 font-medium text-gray-900">
                    {{ feature.name }}
                  </p>
                </dt>
                <dd class="mt-2 ml-16 text-base text-gray-500">
                  {{ feature.description }}
                </dd>
              </div>
            </dl>
          </div>
        </div>
      </div>
    </section> -->
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import HeroIcon from "@/components/common/HeroIcon.vue";
import IButton from "@/components/common/IButton.vue";
import {
  AnnotationIcon,
  GlobeAltIcon,
  LightningBoltIcon,
  ScaleIcon,
} from "@heroicons/vue/outline";
export default defineComponent({
  components: {
    HeroIcon,
    IButton,
    AnnotationIcon,
    GlobeAltIcon,
    LightningBoltIcon,
    ScaleIcon,
  },
  setup() {
    const features = [
      {
        name: "Actualizacion de datos de contacto",
        description:
          "Dar cumplimiento al acuerdo 00/2022 por el que se solicita proporcionar un domicilio para oir y recibir notificaciones.",
        icon: "GlobeAltIcon",
      },
      {
        name: "Convocatoria del programa Poliolimpiadas 2022",
        description:
          "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis ratione.",
        icon: "ScaleIcon",
      },
      {
        name: "Convocatoria del programa Conclusion de Servicio 2023",
        description:
          "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis ratione.",
        icon: "LightningBoltIcon",
      },
      {
        name: "Programa Jefes de Sector 2023",
        description:
          "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis ratione.",
        icon: "AnnotationIcon",
      },
    ];

    return { features };
  },
});
</script>
