import axios from "axios"

const getWeather = (capital) => axios.get(`https://wttr.in/${capital}?format=%t+%w+%C`).then(res => res.data)

export default { getWeather }