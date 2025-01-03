import { useState, useEffect } from "react"
import SearchSection from "./FilterSection"
import AddSection from "./AddSection"
import ResultSection from "./ResultSection"
import phonebookService from "./services/phonebook"

const App = () => {
    const [persons, setPersons] = useState([])
    const [person, setPerson] = useState({ name: '', number: '' })
    const [filter, setFilter] = useState('')
    const [status, setStatus] = useState({ msg: null, isError: false })

    useEffect(() => {
        phonebookService
            .getPersons()
            .then(res => setPersons(res))
    }, [])

    const onSubmit = (event) => {
        event.preventDefault()

        const value = persons.find(p => p.name === person.name)

        if (value) {
            const message = person.name
                + " is already added to phonebook,"
                + " replace the old number with a new one?"
            if (confirm(message)) {
                phonebookService
                    .updatePerson(value.id, person)
                    .then(res => {
                        setPersons(prev => prev.map(p => p.id === res.id ? res : p))
                        setStatus({ msg: `Updated ${res.name}`, isError: false })
                        setTimeout(() => setStatus({ msg: null, isError: false }), 5000)
                    })
                    .catch(() => {
                        setStatus({ msg: `Information of ${person.name} has already been removed from server`, isError: true })
                        setTimeout(() => setStatus({ msg: null, isError: false }), 5000)
                    })
            }
        } else {
            phonebookService
                .addPerson(person)
                .then(res => {
                    setPersons([...persons, res])
                    setStatus({ msg: `Added ${res.name}`, isError: false })
                    setTimeout(() => setStatus({ msg: null, isError: false }), 5000)
                })
                .catch(error => {
                    setStatus({ msg: error.message, isError: true })
                    setTimeout(() => setStatus({ msg: null, isError: false }), 5000)
                })
        }

        setPerson({ name: '', number: '' })
    }

    const onName = (event) => setPerson((prev) => ({ ...prev, name: event.target.value }))
    const onNumber = (event) => setPerson((prev) => ({ ...prev, number: event.target.value }))
    const onFilter = (event) => setFilter(event.target.value)

    const onDelete = (id) => {
        if (confirm(`Delete ${persons.find(person => person.id === id).name} ?`)) {
            phonebookService
                .deletePerson(id)
                .then(res => {
                    setPersons(persons.filter(person => person.id !== res.id))
                    setStatus({ msg: `Deleted ${res.name}`, isError: false })
                    setTimeout(() => setStatus({ msg: null, isError: false }), 5000)
                })
                .catch(error => {
                    setStatus({ msg: error.message, isError: true })
                    setTimeout(() => setStatus({ msg: null, isError: false }), 5000)
                })
        }
    }

    return (
        <div>
            <SearchSection
                status={status}
                filter={filter}
                onFilter={onFilter}
            />
            <AddSection
                person={person}
                onSubmit={onSubmit}
                onName={onName}
                onNumber={onNumber}
            />
            <ResultSection
                persons={persons}
                filter={filter}
                onDelete={onDelete}
            />
        </div>
    )
}

export default App