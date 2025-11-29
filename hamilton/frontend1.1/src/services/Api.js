/* eslint-disable no-underscore-dangle */
/* eslint-disable no-param-reassign */
/* eslint-disable no-unused-vars */
/* eslint-disable no-prototype-builtins */
import axios from 'axios'
import { useAuthenticationStore } from "@/store/authentication";
import { createClient } from '@supabase/supabase-js'

const baseUrl = `https://hechosrelevantes.ssc.cdmx.gob.mx:8443/api/v1`;
// const supabaseUrl = 'http://localhost:8000'
// const supabaseKey = process.env.SUPABASE_KEY
// const supabase = createClient(supabaseUrl, supabaseKey)

const instance = axios.create({
  baseURL: baseUrl,
})

instance.interceptors.request.use((config, next) => {
  if (localStorage.hasOwnProperty('perfil-authentication-store') && JSON.parse(localStorage.getItem('perfil-authentication-store')).authentication) {
    config.headers.Authorization = [
      'token', JSON.parse(localStorage.getItem('perfil-authentication-store')).authentication,
    ].join(' ')
  } else {
    delete config.headers.Authorization
  }
  return config
}, error => Promise.reject(error))

instance.interceptors.response.use(response => response, error => {
  const originalRequest = error.config
  // TODO ADD REFRESH TOKEN METHOD
  if (error.response && error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true
    const store = useAuthenticationStore()
    store.$reset()
    window.location.href = '/login';

    //   const rToken = authUser.auth.isAuthenticated.refresh_token
    //   // console.log(`attempt to refresh token here - ${process.env.SERVER_URL}?refresh_token=${rToken}`)
    //   return axios.post(`${process.env.SERVER_URL}/oauth/access_token?grant_type=refresh_token&refresh_token=${rToken}`)
    //     .then(({ data }) => {
    //       // console.log('==got the following token back: ' + data.access_token + '___________________________________________' + authUser.user.token)

    //       store.dispatch('user/setToken', data.access_token)

    //       const authUser1 = JSON.parse(window.localStorage.getItem('plataforma-perfil'))

    //       if (data.access_token === authUser1.user.token) {
    //         console.log('Great news the underlying user token has now been updated meaning the user has now been re-authenticated')
    //       }

    //       axios.defaults.headers.common.Authorization = `Bearer ${data.access_token}`
    //       originalRequest.headers.Authorization = `Bearer ${data.access_token}`
    //       return axios(originalRequest)
    //     })
  }
  return Promise.reject(error)
})

export default () => instance
