<template>
  <el-upload
    ref="uploadRef"
    :class="`upload-demo-${nombre}`"
    drag
    :auto-upload="false"
    :on-change="onSelectFile"
    :on-remove="onRemove"
    :on-success="onSuccess"
    :limit="1"
  >
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <div class="el-upload__text">
      Arrastra un archivo aqui o <em>haz clic para subir</em>
    </div>
    <template #tip>
      <div class="el-upload__tip block md:flex md:justify-between">
        <span> Archivos PNG, JPG o PDF no mayores a 1MB </span>
        <span v-if="fileRequired" class="text-red-500">
          {{ fileHelperText }}
        </span>
      </div>
    </template>
    <template v-slot:file="{ file }">
      <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
        <ul
          role="list"
          class="border border-gray-200 rounded-md divide-y divide-gray-200"
        >
          <li class="pl-3 pr-4 py-3 flex items-center justify-between text-sm">
            <div class="w-0 flex-1 flex items-center">
              <hero-icon
                icon="PaperClipIcon"
                class="flex-shrink-0 h-5 w-5 text-gray-400"
              ></hero-icon>
              <span class="ml-2 flex-1 w-0 truncate">
                {{ file.name }}
              </span>
            </div>
            <div class="ml-4 flex-shrink-0 flex space-x-4">
              <button
                @click="deleteFile(file)"
                type="button"
                class="
                  bg-white
                  rounded-md
                  font-medium
                  text-maincolor-500
                  hover:text-maincolor-400
                  focus:outline-none
                  focus:ring-2
                  focus:ring-offset-2
                  focus:ring-maincolor-400
                "
              >
                Remover
              </button>
            </div>
          </li>
        </ul>
      </dd>
    </template>
  </el-upload>
</template>
<script>
import { ref, watch } from "vue";
import "element-plus/es/components/upload/style/css";
import { ElUpload, ElIcon } from "element-plus";
import { UploadFilled } from "@element-plus/icons-vue";
import HeroIcon from "@/components/common/HeroIcon.vue";
export default {
  emits: ["update:modelValue"],
  components: {
    ElUpload,
    ElIcon,
    UploadFilled,
    HeroIcon,
  },
  props: {
    nombre: String,
    modelValue: {
      type: Object,
      default: () => {},
    },
  },
  setup(props, { emit }) {
    const currentValue = ref(null);
    const fileRequired = ref(false);
    const uploadRef = ref(null);

    const fileHelperText = ref(
      "El documento de comprobante de domicilio el obligatorio"
    );

    watch(currentValue, (newValue, oldValue) => {
      let val = newValue;
      emit("update:modelValue", val);
    });

    watch(
      () => props.modelValue,
      (newValue, oldValue) => {
        if (newValue !== oldValue) {
          currentValue.value = newValue;
        }
      },
      { immediate: true }
    );

    function deleteFile(file) {
      uploadRef.value?.handleRemove(file);
    }

    function clearFiles() {
      console.log("clearfiles");
      uploadRef.value?.clearFiles();
    }

    function onSuccess(evt) {
      console.log("onSuccess");
      console.log(evt);
    }

    function onRemove(evt) {
      console.log("onRemove");
      console.log(evt);
      currentValue.value = null;
    }

    function onSelectFile(evt) {
      console.log("onSelectFile");
      console.log(evt);
      if (evt.raw) {
        currentValue.value = evt.raw;
        const elUploadDragger = document.querySelectorAll(
          `.upload-demo-${props.nombre} .el-upload-dragger`
        )[0];
        console.log(elUploadDragger);
        elUploadDragger.style.cssText = " ";
        fileHelperText.value = "";
      } else {
        fileHelperText.value = "El documento no es un archivo valido";
      }
    }
    return {
      onSelectFile,
      onRemove,
      onSuccess,
      fileRequired,
      deleteFile,
      clearFiles,
      uploadRef

    };
  },
};
</script>