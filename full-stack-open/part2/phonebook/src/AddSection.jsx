const AddSection = ({ person, onSubmit, onName, onNumber }) => {
    return (
        <section>
            <h2>Add a new</h2>
            <form onSubmit={onSubmit}>
                <div>
                    <label htmlFor="name">Name: </label>
                    <input id="name" value={person.name} onChange={onName} />
                </div>
                <div>
                    <label htmlFor="number">Number: </label>
                    <input id="number" value={person.number} onChange={onNumber} />
                </div>
                <div>
                    <button type="submit">add</button>
                </div>
            </form>
        </section>
    )
}

export default AddSection