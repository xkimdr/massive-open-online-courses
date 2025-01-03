import axios from "axios"

const baseURL = "http://localhost:3001/persons"

const getPersons = () => axios.get(baseURL).then(res => res.data)
const addPerson = (obj) => axios.post(baseURL, obj).then(res => res.data)
const updatePerson = (id, obj) => axios.put(`${baseURL}/${id}`, obj).then(res => res.data)
const deletePerson = (id) => axios.delete(`${baseURL}/${id}`).then(res => res.data)

export default { getPersons, addPerson, updatePerson, deletePerson }
