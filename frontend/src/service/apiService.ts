import axios from 'axios'

const ApiService = axios.create({
    baseURL: process.env.VUE_APP_API_URL,
    headers: {
        Accept: 'application/json',
    },
})

ApiService.interceptors.response.use(response => {
    return response
},
    async error =>{
    return Promise.reject(error.response.data)
    })

export default ApiService
