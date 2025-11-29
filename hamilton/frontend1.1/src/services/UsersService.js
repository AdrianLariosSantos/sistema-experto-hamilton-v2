import Api from '@/services/Api'

const resource = 'authentication'

export default {
  logout() {
    return Api().post(`${resource}/logout/`)
  },
  login(form) {
    return Api().post(`${resource}/login/`, form)
  },
  register(form) {
    return Api().post(`${resource}/registration/`, form)
  },
  getPhoto(numeroEmpleado) {
    return Api().get(`datos/contacto/empleado/${numeroEmpleado}/picture`)
  },
  getAccountData() {
    return Api().get(`datos/empleado/account`)
  },
}
