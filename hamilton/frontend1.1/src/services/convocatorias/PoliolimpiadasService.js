import Api from '@/services/Api'

const resource = 'convocatorias/poli-olimpiadas'

export default {
  create (form) {
    return Api().post(`${resource}/inscripcion/`, form)
  },
  addPrueba (form) {
    return Api().post(`${resource}/inscripcion/prueba/`, form)
  },
  addEquipo (form) {
    return Api().post(`${resource}/equipo/`, form)
  },
  getEquipos () {
    return Api().get(`${resource}/equipo/`)
  },
  getExistsData () {
    return Api().get(`${resource}/inscripcion/exists`)
  },
  getAllPruebas () {
    return Api().get(`${resource}/catalogos/prueba/all`)
  },
  getAllDisciplinas () {
    return Api().get(`${resource}/catalogos/disciplina/all`)
  },
  getAllPruebasInscripcion () {
    return Api().get(`${resource}/inscripcion/prueba/`)
  },
  getAllIntegrantesEquipo (params) {
    return Api().get(`${resource}/equipo/integrante/`, { params })
  },
  addIntegrante (form) {
    return Api().post(`${resource}/equipo/integrante/`, form)
  },
  removerPrueba (id) {
    return Api().delete(`${resource}/inscripcion/prueba/${id}/`)
  },
  removerIntegrante (id) {
    return Api().delete(`${resource}/equipo/integrante/${id}/`)
  },
}
