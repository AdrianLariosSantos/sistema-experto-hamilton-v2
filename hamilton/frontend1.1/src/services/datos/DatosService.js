import Api from '@/services/Api'

const resource = 'datos/contacto'

export default {
  getDatosEmpleadoSap() {
    return Api().get(`${resource}/empleado/sap`)
  },
  getExistsData() {
    return Api().get(`${resource}/empleado/exists`)
  },
  validarCorreoElectronico(body) {
    return Api().post(`${resource}/validar/correo/`, body)
  },
}
