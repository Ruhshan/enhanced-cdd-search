import axios from 'axios'

const ApiService = axios.create({
    baseURL: process.env.VUE_APP_API_URL,
    headers: {
        Accept: 'application/json',
    },
})

ApiService.interceptors.response.use(response => {
    console.log('API url '+process.env.VUE_APP_API_URL)
    return response
})

export default ApiService
