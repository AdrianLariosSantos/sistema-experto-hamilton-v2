import Api from '@/services/Api'

const resource = 'juez-civico'

export default {
  getAlcaldiasJC() {
    return Api().get(`${resource}/alcaldias`)
  },
}
