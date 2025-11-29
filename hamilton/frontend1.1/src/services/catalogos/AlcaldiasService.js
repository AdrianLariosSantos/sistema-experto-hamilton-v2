import Api from '@/services/Api'
// import {AlcaldiaResponse} from './AlcaldiaResponse' 

const resource = 'catalogos/alcaldia'

export default {
  getAlcaldias() {
    return Api().get(`${resource}/all`)
  },
}
