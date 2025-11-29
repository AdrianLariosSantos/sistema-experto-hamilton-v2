<template>
  <div>
    <div class="bg-white rounded-lg overflow-hidden">
      <div
        class="
          divide-y divide-gray-200
          lg:grid lg:grid-cols-12 lg:divide-y-0 lg:divide-x
        "
      >
        <TabGroup>
          <aside class="py-6 lg:col-span-3">
            <nav class="space-y-1">
              <TabList class="space-y-1">
                <Tab
                  v-for="item in subNavigation"
                  :key="item.name"
                  :class="[
                    item.current
                      ? 'bg-maincolor-50 border-maincolor-500 text-maincolor-700 hover:bg-maincolor-50 hover:text-maincolor-700'
                      : 'border-transparent text-gray-900 hover:bg-gray-50 hover:text-gray-900',
                    'group border-l-4 px-3 py-2 flex items-center text-sm font-medium w-full',
                  ]"
                >
                  <component
                    :is="item.icon"
                    :class="[
                      item.current
                        ? 'text-maincolor-500 group-hover:text-maincolor-500'
                        : 'text-gray-400 group-hover:text-gray-500',
                      'flex-shrink-0 -ml-1 mr-3 h-6 w-6',
                    ]"
                    aria-hidden="true"
                  />
                  <span class="truncate">
                    {{ item.name }}
                  </span>
                </Tab>
              </TabList>
            </nav>
          </aside>
          <TabPanels class="divide-y divide-gray-200 lg:col-span-9">
            <TabPanel>
              <form action="#" method="POST">
                <!-- Profile section -->
                <div class="py-6 px-4 sm:p-6 lg:pb-8">
                  <div>
                    <h2 class="text-lg leading-6 font-medium text-gray-900">
                      Perfil
                    </h2>
                    <p class="mt-1 text-sm text-gray-500">
                      Visualiza informacion sobre los datos de tu perfil, area
                      de adscripcion, etc.
                    </p>
                  </div>

                  <div class="mt-6 flex flex-col lg:flex-row">
                    <div class="flex-grow space-y-6">
                      <div class="w-full">
                        <label-form
                          text="Nombre de usuario"
                          class="text-left mt-0"
                        />
                        <text-input
                          width="max-w-3xl"
                          :required="true"
                          v-model="form.username"
                          disabled
                        />
                      </div>

                      <div>
                        <div class="mt-6 grid grid-cols-12 gap-6">
                          <div class="col-span-12 sm:col-span-6">
                            <label-form text="Nombre" class="text-left mt-0" />
                            <text-input
                              width="max-w-3xl"
                              :required="true"
                              v-model="form.first_name"
                              disabled
                            />
                          </div>
                          <div class="col-span-12 sm:col-span-6">
                            <label-form
                              text="Primer apellido"
                              class="text-left mt-0"
                            />
                            <text-input
                              width="max-w-3xl"
                              :required="true"
                              v-model="form.last_name"
                              disabled
                            />
                          </div>
                        </div>
                      </div>
                    </div>

                    <div
                      class="
                        mt-6
                        mb-6
                        md:mb-0
                        flex-grow
                        lg:mt-0 lg:ml-6 lg:flex-grow-0 lg:flex-shrink-0
                      "
                    >
                      <p
                        class="text-sm font-medium text-gray-700"
                        aria-hidden="true"
                      >
                        Fotografia
                      </p>
                      <div class="mt-1 lg:hidden">
                        <div class="flex items-center">
                          <div
                            class="
                              flex-shrink-0
                              inline-block
                              rounded-full
                              overflow-hidden
                              h-12
                              w-12
                            "
                            aria-hidden="true"
                          >
                            <img
                              class="rounded-full h-full w-full object-cover"
                              :src="fotografia.fotografia_b64"
                              alt=""
                            />
                          </div>
                          <!-- <div class="ml-5 rounded-md shadow-sm">
                            <div
                              class="
                                group
                                relative
                                border border-gray-300
                                rounded-md
                                py-2
                                px-3
                                flex
                                items-center
                                justify-center
                                hover:bg-gray-50
                                focus-within:ring-2
                                focus-within:ring-offset-2
                                focus-within:ring-sky-500
                              "
                            >
                              <label
                                for="mobile-user-photo"
                                class="
                                  relative
                                  text-sm
                                  leading-4
                                  font-medium
                                  text-gray-700
                                  pointer-events-none
                                "
                              >
                                <span>Change</span>
                                <span class="sr-only"> user photo</span>
                              </label>
                              <input
                                id="mobile-user-photo"
                                name="user-photo"
                                type="file"
                                class="
                                  absolute
                                  w-full
                                  h-full
                                  opacity-0
                                  cursor-pointer
                                  border-gray-300
                                  rounded-md
                                "
                              />
                            </div>
                          </div> -->
                        </div>
                      </div>

                      <div
                        class="
                          hidden
                          relative
                          rounded-full
                          overflow-hidden
                          lg:block
                          
                        "
                      >
                        <img
                          class="relative rounded-full object-cover w-40 h-40"
                          :src="fotografia.fotografia_b64"
                          alt=""
                        />
                        <!-- <label
                          for="desktop-user-photo"
                          class="
                            absolute
                            inset-0
                            w-full
                            h-full
                            bg-black bg-opacity-75
                            flex
                            items-center
                            justify-center
                            text-sm
                            font-medium
                            text-white
                            opacity-0
                            hover:opacity-100
                            focus-within:opacity-100
                          "
                        >
                          <span>Change</span>
                          <span class="sr-only"> user photo</span>
                          <input
                            type="file"
                            id="desktop-user-photo"
                            name="user-photo"
                            class="
                              absolute
                              inset-0
                              w-full
                              h-full
                              opacity-0
                              cursor-pointer
                              border-gray-300
                              rounded-md
                            "
                          />
                        </label> -->
                      </div>
                    </div>
                  </div>

                  <div class="grid grid-cols-12 gap-6">
                    <div class="col-span-12 sm:col-span-6">
                      <label-form
                        text="Segundo Apellido"
                        class="text-left mt-0"
                      />
                      <text-input
                        width="w-full"
                        :required="true"
                        v-model="form.second_surname"
                        disabled
                      />
                    </div>
                    <div class="col-span-12 sm:col-span-6">
                      <label-form
                        text="Correo electronico"
                        class="text-left mt-0"
                      />
                      <text-input
                        width="w-full"
                        :required="true"
                        v-model="form.email"
                        disabled
                      />
                    </div>
                  </div>
                </div>

                <!-- Privacy section -->
              </form>
            </TabPanel>
          </TabPanels>
        </TabGroup>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  Switch,
  SwitchDescription,
  SwitchGroup,
  SwitchLabel,
} from "@headlessui/vue";
import { SearchIcon } from "@heroicons/vue/solid";
import {
  BellIcon,
  CogIcon,
  CreditCardIcon,
  KeyIcon,
  MenuIcon,
  UserCircleIcon,
  ViewGridAddIcon,
  XIcon,
} from "@heroicons/vue/outline";
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from "@headlessui/vue";
import UsersService from "@/services/UsersService";

export default defineComponent({
  components: {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
    Switch,
    SwitchDescription,
    SwitchGroup,
    SwitchLabel,
    BellIcon,
    CogIcon,
    CreditCardIcon,
    KeyIcon,
    MenuIcon,
    UserCircleIcon,
    ViewGridAddIcon,
    XIcon,
    SearchIcon,
    TabGroup,
    TabList,
    Tab,
    TabPanels,
    TabPanel,
  },
  setup() {
    const isLoadingPhoto = ref(false);

    const subNavigation = [
      { name: "Perfil", href: "#", icon: UserCircleIcon, current: true },
      // { name: "Cuenta", href: "#", icon: CogIcon, current: false },
      // { name: "Contraseña", href: "#", icon: KeyIcon, current: false },
      // { name: "Notificaciones", href: "#", icon: BellIcon, current: false },
    ];
    const user = {
      name: "Debbie Lewis",
      handle: "deblewis",
      email: "debbielewis@example.com",
      imageUrl:
        "https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=320&h=320&q=80",
    };

    const form = ref({
      username: null,
      first_name: null,
      last_name: null,
      second_surname: null,
      email: null,
      numero_empleado: null,
    });

    const fotografia = ref({
      fotografia_b64: null,
    });

    function getPhoto() {
      isLoadingPhoto.value = true;
      UsersService.getPhoto(form.value.numero_empleado)
        .then((response) => {
          const { data } = response;
          if (data.status) {
            fotografia.value.fotografia_b64 = `data:image/jpeg;base64,${data.imagen}`;
          }
        })
        .finally(() => {
          isLoadingPhoto.value = false;
        });
    }

    async function getAccountData() {
      return UsersService.getAccountData()
        .then((response) => {
          const { data } = response;
          form.value = data.data
        })
    }

    async function getProfileData() {
      await getAccountData();
      getPhoto();
    }
    return { subNavigation, user, fotografia, form, getProfileData };
  },
  mounted() {
    this.getProfileData();
  },
});
</script>
