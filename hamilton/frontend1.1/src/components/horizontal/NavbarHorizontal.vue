<template>
  <div>
    <Disclosure as="nav" class="bg-maincolor-500" v-slot="{ open }">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img
                class="h-10 w-auto"
                src="@/assets/images/brand/logo-ssc-blanco-recortado.png"
                alt="Logo SSC"
              />
            </div>
            <div class="hidden md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <div v-for="item in navigation" :key="item.title">
                  <div v-if="!item.hasChildren">
                    <a
                      @click.prevent="router.push({ name: item.route })"
                      :class="currentRouteClass(item.route)"
                      class="cursor-pointer"
                      :aria-current="item.current ? 'page' : undefined"
                      >{{ item.title }}</a
                    >
                  </div>
                  <div v-else>
                    <Popover class="relative" v-slot="{ open }">
                      <PopoverButton
                        class="inline-flex items-center"
                        :class="currentRouteClass(item.route)"
                      >
                        <span>{{ item.title }}</span>
                        <ChevronDownIcon
                          class="-mr-1 ml-2 h-5 w-5"
                          :class="open ? 'transform rotate-180' : ''"
                        />
                      </PopoverButton>

                      <transition
                        enter-active-class="transition duration-200 ease-out"
                        enter-from-class="translate-y-1 opacity-0"
                        enter-to-class="translate-y-0 opacity-100"
                        leave-active-class="transition duration-150 ease-in"
                        leave-from-class="translate-y-0 opacity-100"
                        leave-to-class="translate-y-1 opacity-0"
                      >
                        <PopoverPanel
                          class="
                            absolute
                            z-10
                            -left-full
                            mt-1
                            w-screen
                            max-w-4xl
                            shadow-md
                          "
                        >
                          <div
                            class="
                              rounded-lg
                              bg-gray-200
                              overflow-hidden
                              shadow
                              divide-y divide-gray-200
                              sm:divide-y-0 sm:grid sm:grid-cols-2 sm:gap-px
                            "
                            v-if="item.children.length > 0"
                          >
                            <div
                              v-for="(child, actionIdx) in item.children"
                              :key="child.title"
                              :class="[
                                actionIdx === 0
                                  ? 'rounded-tl-lg rounded-tr-lg sm:rounded-tr-none'
                                  : '',
                                actionIdx === 1 ? 'sm:rounded-tr-lg' : '',
                                actionIdx === item.children - 2
                                  ? 'sm:rounded-bl-lg'
                                  : '',
                                actionIdx === item.children - 1
                                  ? 'rounded-bl-lg rounded-br-lg sm:rounded-bl-none'
                                  : '',

                                'relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-500',
                              ]"
                            >
                              <div>
                                <span
                                  :class="[
                                    child.iconBackground,
                                    child.iconForeground,
                                    'rounded-lg inline-flex p-3 ring-4 ring-white',
                                  ]"
                                >
                                  <hero-icon
                                    :icon="child.icon"
                                    class="group-hover:animate-bounce h-6 w-6"
                                  ></hero-icon>
                                </span>
                              </div>
                              <div class="mt-4">
                                <h3 class="text-lg font-medium">
                                  <a
                                    @click.prevent="
                                      router.push({ name: child.route })
                                    "
                                    class="focus:outline-none cursor-pointer"
                                  >
                                    <!-- Extend touch target to entire panel -->
                                    <span
                                      class="absolute inset-0"
                                      aria-hidden="true"
                                    />
                                    {{ child.title }}
                                  </a>
                                </h3>
                                <p
                                  class="
                                    mt-2
                                    text-sm
                                    font-semibold
                                    text-gray-500
                                    group-hover:text-gray-700
                                  "
                                >
                                  {{ child.description }}
                                </p>
                              </div>
                              <span
                                v-if="child.featured"
                                class="
                                  pointer-events-none
                                  absolute
                                  top-6
                                  right-6
                                  text-orange-400
                                  font-bold
                                  text-lg
                                "
                                aria-hidden="true"
                              >
                                DESTACADO
                              </span>
                              <span
                                v-else
                                class="
                                  pointer-events-none
                                  absolute
                                  top-6
                                  right-6
                                  text-gray-300
                                  group-hover:text-gray-400
                                "
                                aria-hidden="true"
                              >
                                <svg
                                  class="h-6 w-6"
                                  xmlns="http://www.w3.org/2000/svg"
                                  fill="currentColor"
                                  viewBox="0 0 24 24"
                                >
                                  <path
                                    d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z"
                                  />
                                </svg>
                              </span>
                            </div>
                          </div>
                        </PopoverPanel>
                      </transition>
                    </Popover>
                  </div>
                </div>
                <div></div>
              </div>
            </div>
          </div>
          <div class="hidden md:block">
            <div class="ml-4 flex items-center md:ml-6">
              <button
                type="button"
                class="
                  bg-maincolor-600
                  p-1
                  rounded-full
                  text-maincolor-100
                  hover:text-white
                  focus:outline-none
                  focus:ring-2
                  focus:ring-offset-2
                  focus:ring-offset-maincolor-600
                  focus:ring-white
                "
              >
                <span class="sr-only">View notifications</span>
                <BellIcon class="h-6 w-6" aria-hidden="true" />
              </button>

              <!-- Profile dropdown -->
              <Menu as="div" class="ml-3 relative">
                <div>
                  <MenuButton
                    class="
                      max-w-xs
                      bg-maincolor-600
                      rounded-full
                      flex
                      items-center
                      text-sm text-white
                      focus:outline-none
                      focus:ring-2
                      focus:ring-offset-2
                      focus:ring-offset-maincolor-600
                      focus:ring-white
                    "
                  >
                    <span class="sr-only">Open user menu</span>
                    <img
                      class="h-8 w-8 rounded-full"
                      src="@/assets/images/misc/default-avatar.jpg"
                      alt=""
                    />
                  </MenuButton>
                </div>
                <transition
                  enter-active-class="transition ease-out duration-100"
                  enter-from-class="transform opacity-0 scale-95"
                  enter-to-class="transform opacity-100 scale-100"
                  leave-active-class="transition ease-in duration-75"
                  leave-from-class="transform opacity-100 scale-100"
                  leave-to-class="transform opacity-0 scale-95"
                >
                  <MenuItems
                    class="
                      origin-top-right
                      absolute
                      right-0
                      mt-2
                      w-48
                      rounded-md
                      shadow-lg
                      py-1
                      bg-white
                      ring-1 ring-black ring-opacity-5
                      focus:outline-none
                    "
                  >
                    <MenuItem v-slot="{ active }">
                      <a
                        @click="router.push({ name: 'usuarioPerfil' })"
                        :class="[
                          active ? 'bg-gray-100' : '',
                          'block px-4 py-2 text-sm text-gray-700 cursor-pointer',
                        ]"
                        >Mi Perfil</a
                      >
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                      <a
                        href="item.href"
                        :class="[
                          active ? 'bg-gray-100' : '',
                          'block px-4 py-2 text-sm text-gray-700',
                        ]"
                        >Ajustes</a
                      >
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                      <a
                        @click="cerrarSesion"
                        class="cursor-pointer"
                        :class="[
                          active ? 'bg-gray-100' : '',
                          'block px-4 py-2 text-sm text-gray-700',
                        ]"
                        >Cerrar sesion</a
                      >
                    </MenuItem>
                  </MenuItems>
                </transition>
              </Menu>
            </div>
          </div>
          <div class="-mr-2 flex md:hidden">
            <!-- Mobile menu button -->
            <DisclosureButton
              class="
                bg-maincolor-600
                inline-flex
                items-center
                justify-center
                p-2
                rounded-md
                text-maincolor-200
                hover:text-white hover:bg-maincolor-500 hover:bg-opacity-75
                focus:outline-none
                focus:ring-2
                focus:ring-offset-2
                focus:ring-offset-maincolor-600
                focus:ring-white
              "
            >
              <span class="sr-only">Open main menu</span>
              <MenuIcon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
              <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
            </DisclosureButton>
          </div>
        </div>
      </div>

      <DisclosurePanel class="md:hidden">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
          <div v-for="item in navigation" :key="item.title">
            <div v-if="!item.hasChildren">
              <DisclosureButton
                as="a"
                @click.prevent="router.push({ name: item.route })"
                class="block cursor-pointer"
                :class="currentRouteClass(item.route)"
                >{{ item.title }}</DisclosureButton
              >
            </div>
            <div v-else>
              <Disclosure>
                <DisclosureButton
                  class="block w-full text-left"
                  :class="currentRouteClass(item.route)"
                >
                  {{ item.title }}
                </DisclosureButton>
                <DisclosurePanel
                  v-if="item.children.length > 0"
                  class="block px-3 py-2 bg-maincolor-300 rounded-md"
                >
                  <DisclosureButton
                    @click.prevent="router.push({ name: child.route })"
                    class="block w-full text-left"
                    :class="currentRouteClass(item.route)"
                    v-for="child in item.children"
                    :key="child.title"
                  >
                    {{ child.title }}
                  </DisclosureButton>
                </DisclosurePanel>
              </Disclosure>
            </div>
          </div>
        </div>
        <div class="pt-4 pb-3 border-t border-maincolor-700">
          <div class="flex items-center px-5">
            <div class="flex-shrink-0">
              <img class="h-10 w-10 rounded-full" :src="user.imageUrl" alt="" />
            </div>
            <div class="ml-3">
              <div class="text-base font-medium text-white">
                {{ user.name }}
              </div>
              <div class="text-sm font-medium text-maincolor-300">
                {{ user.email }}
              </div>
            </div>
            <button
              type="button"
              class="
                ml-auto
                bg-maincolor-600
                flex-shrink-0
                p-1
                border-2 border-transparent
                rounded-full
                text-maincolor-200
                hover:text-white
                focus:outline-none
                focus:ring-2
                focus:ring-offset-2
                focus:ring-offset-maincolor-600
                focus:ring-white
              "
            >
              <span class="sr-only">View notifications</span>
              <BellIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div class="mt-3 px-2 space-y-1">
            <DisclosureButton
              as="a"
              @click="router.push({ name: 'usuarioPerfil' })"
              class="
                block
                px-3
                py-2
                rounded-md
                text-base
                font-medium
                text-white
                hover:bg-maincolor-500 hover:bg-opacity-75
              "
              >Mi Perfil</DisclosureButton
            >
            <DisclosureButton
              as="a"
              to="#"
              class="
                block
                px-3
                py-2
                rounded-md
                text-base
                font-medium
                text-white
                hover:bg-maincolor-500 hover:bg-opacity-75
              "
              >Ajustes</DisclosureButton
            >
            <DisclosureButton
              as="a"
              to="#"
              class="
                block
                px-3
                py-2
                rounded-md
                text-base
                font-medium
                text-white
                hover:bg-maincolor-500 hover:bg-opacity-75
              "
              >Cerrar sesion</DisclosureButton
            >
          </div>
        </div>
      </DisclosurePanel>
    </Disclosure>

    <header class="bg-white shadow">
      <div
        class="
          max-w-7xl
          mx-auto
          py-6
          px-4
          sm:px-6
          lg:px-8
          block
          md:flex
          items-center
        "
      >
        <h1 class="text-3xl font-bold leading-tight text-gray-900">
          {{ route.meta.pageTitle }}
        </h1>
        <breadcrumbs-component
          v-if="hasBreadcrumbs"
          :breadcrumbs="route.meta.breadcrumb"
        />
      </div>
    </header>
  </div>
</template>
<script lang="ts">
import { computed, defineComponent } from "vue";
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  Popover,
  PopoverButton,
  PopoverPanel,
} from "@headlessui/vue";
import {
  AcademicCapIcon,
  BadgeCheckIcon,
  CashIcon,
  ClockIcon,
  ReceiptRefundIcon,
  UsersIcon,
} from "@heroicons/vue/outline";
import { BellIcon, MenuIcon, XIcon } from "@heroicons/vue/outline";
import { navigationMenu } from "@/navigation/index.ts";
import { useRouter, useRoute } from "vue-router";
import { ChevronDownIcon } from "@heroicons/vue/solid";
import HeroIcon from "../../components/common/HeroIcon.vue";
import BreadcrumbsComponent from "./components/BreadcrumbsComponent.vue";
import UsersService from "@/services/UsersService";
import { useAuthenticationStore } from "@/store/authentication";
import { useUserStore } from "@/store/user";

export default defineComponent({
  components: {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
    BellIcon,
    MenuIcon,
    XIcon,
    Popover,
    PopoverButton,
    PopoverPanel,
    AcademicCapIcon,
    BadgeCheckIcon,
    CashIcon,
    ClockIcon,
    ReceiptRefundIcon,
    UsersIcon,
    ChevronDownIcon,
    HeroIcon,
    BreadcrumbsComponent,
  },
  setup() {
    const router = useRouter();
    const route = useRoute();

    const authStore = useAuthenticationStore();
    const userStore = useUserStore();

    const user = {
      name: "Tom Cook",
      email: "tom@example.com",
      imageUrl: "@/assets/images/misc/default-avatar.jpg",
    };
    const navigation = navigationMenu;

    const userNavigation = [
      { name: "Your Profile", href: "#" },
      { name: "Settings", href: "#" },
      { name: "Sign out", href: "#" },
    ];

    const hasBreadcrumbs = computed(() => {
      return Object.prototype.hasOwnProperty.call(route.meta, "breadcrumb");
    });

    function currentRouteClass(routeNav) {
      let cls = "px-3 py-2 rounded-md text-sm font-medium ";
      if (route.name === routeNav) {
        cls += "bg-maincolor-700 text-white";
      } else {
        cls += "text-white hover:bg-maincolor-500 hover:bg-opacity-75";
      }

      return cls;
    }

    function cerrarSesion() {
      UsersService.logout()
        .then(() => {
          authStore.$reset();
          userStore.$reset();
          router.push({ name: "login" });
        })
        .catch(() => {
          authStore.$reset();
          userStore.$reset();
          router.push({ name: "login" });
          // console.log(error);
          // const { response } = error.response;
          // if (response.status === 400) {
          //   Object.assign(errors.value, response.data);
          // }
        })
        .finally(() => {
          // isLoading.value = false;
        });
    }

    return {
      user,
      navigation,
      userNavigation,
      currentRouteClass,
      route,
      router,
      hasBreadcrumbs,
      cerrarSesion,
    };
  },
});
</script>
