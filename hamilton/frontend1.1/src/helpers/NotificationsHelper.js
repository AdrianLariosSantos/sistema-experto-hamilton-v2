import { useNotificationStore } from "@/store/notifications"

export const useNotificationHelper = (

) => {

  function showNotification ({duration = 4000, variant = 'success', title = "Titulo", message = "Mensaje"} = {}) {

    const store = useNotificationStore()

    store.show = true
    store.variant = variant
    store.title = title
    store.message = message

    setTimeout(() => store.show = false, duration)
  }

  return { showNotification }
}
