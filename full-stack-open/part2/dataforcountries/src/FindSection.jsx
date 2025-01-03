const FindSection = ({ onFilter }) => {
    return (
        <section>
            <label htmlFor="find">find countries: </label>
            <input id="find" type="text" onChange={onFilter} />
        </section>
    )
}

export default FindSection