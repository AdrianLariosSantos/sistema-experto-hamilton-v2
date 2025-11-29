import Api from '@/services/Api'

const resource = 'juez-civico'

export default {
  getColoniasJC(params) {
    return Api().get(`${resource}/colonias`, {
      params: params
    })
  },
}
