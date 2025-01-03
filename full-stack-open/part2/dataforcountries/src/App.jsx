import { useState, useEffect } from "react"
import dataService from "./services/data"
import FindSection from "./FindSection"
import MatchSection from "./MatchSection"

const App = () => {
    const [all, setAll] = useState([])
    const [match, setMatch] = useState([])

    useEffect(() => {
        dataService
            .getAll()
            .then(res => {
                setAll(res.map(x => ({
                    name: x.name.common,
                    capitals: x.capital,
                    area: x.area,
                    languages: x.languages,
                    flags: x.flags
                })))
            })
    }, [])

    const onFilter = (event) => {
        const value = event.target.value
        if (value.length === 0) {
            setMatch([])
        }
        else {
            setMatch(all.filter(x => x.name.toLowerCase().includes(value.toLowerCase())))
        }
    }

    const onShow = (x) => setMatch([x])

    return (
        <div>
            <FindSection onFilter={onFilter} />
            <MatchSection match={match} onShow={onShow} />
        </div>
    )

}

export default App