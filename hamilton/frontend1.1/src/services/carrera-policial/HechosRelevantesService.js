import Api from '@/services/Api'

const resource = 'datos/hechos-relevantes'

export default {
  create(form) {
    return Api().post(`${resource}/`, form)
  },
}
