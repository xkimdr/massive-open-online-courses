const Status = ({ status }) => {
    if (status.msg === null) {
        return null
    }

    const color = (status.isError) ? "red" : "green"

    const style = {
        color: color,
        background: "lightgrey",
        fontSize: 20,
        borderStyle: "solid",
        borderRadius: 5,
        padding: 10,
        marginBottom: 10,
    }

    return (
        <div style={style}>
            {status.msg}
        </div>
    )
}

const FilterSection = ({ status, filter, onFilter }) => {
    return (
        <section>
            <h2>Phonebook</h2>
            <Status status={status} />
            <div>
                <label htmlFor="filter">Filter shown with: </label>
                <input id="filter" value={filter} onChange={onFilter} />
            </div>
        </section>
    )
}

export default FilterSection