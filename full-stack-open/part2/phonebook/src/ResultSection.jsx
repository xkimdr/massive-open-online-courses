const ResultSection = ({ persons, filter, onDelete }) => {
    return (
        <section>
            <h2>Numbers</h2>
            {persons
                .filter((person) => (
                    person.name
                        .toLowerCase()
                        .includes(filter.toLowerCase())
                ))
                .map((person) => (
                    <p key={person.id}>
                        <span>{person.name} {person.number} </span>
                        <button onClick={() => onDelete(person.id)}>delete</button>
                    </p>
                ))
            }
        </section>
    )
}

export default ResultSection