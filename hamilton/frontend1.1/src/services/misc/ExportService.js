import Api from '@/services/Api'

const resource = "exports/download"

export default {

    exportComprobanteAcuerdo0022 (params) {
        return Api().get(`${resource}/comprobante/acuerdo/00-2022`, {
            params,
            responseType: 'blob',
        })
    },
    exportComprobanteInscripcion () {
        return Api().get(`${resource}/convocatorias/poli-olimpiadas/comprobante`, {
            responseType: 'blob',
        })
    },
    exportComprobanteInscripcionEquipo (id) {
        return Api().get(`${resource}/convocatorias/poli-olimpiadas/comprobante-equipo/${id}`, {
            responseType: 'blob',
        })
    },

}