import Api from '@/services/Api'

const resource = 'datos/contacto'

export default {
  create(form) {
    return Api().post(`${resource}/`, form)
  },
}
