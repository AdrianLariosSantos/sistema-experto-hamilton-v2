import Api from '@/services/Api'

const resource = 'juez-civico'

export default {
  getCodigosPostalesJC(params) {
    return Api().get(`${resource}/codigos-postales`, {
      params: params
    })
  },
}
