import { useState, useEffect } from "react";
import weatherService from './services/weather';

const Weather = ({ capital }) => {
    const [weather, setWeather] = useState(null);

    useEffect(() => {
        weatherService.getWeather(capital).then(x => {
            const parts = x.split(" ")
            setWeather(parts)
        })
    }, [capital])

    if (!weather) {
        return <p>Loading weather data...</p>;
    }

    return (
        <section>
            <h2>Weather in {capital}</h2>
            <p>temperature: {weather[0]}</p>
            <p>wind: {weather[1]}</p>
            <p>{weather[2]}</p>
        </section>
    )
}

const Weathers = ({ capitals }) => {
    return (
        <section>
            {capitals.map(x => (<Weather key={x} capital={x} />))}
        </section>
    )
}

const Languages = ({ languages }) => {
    return (
        <>
            {Object
                .entries(languages)
                .map((x) => (<li key={x[0]}>{x[1]}</li>))
            }
        </>
    )
}

const MatchSection = ({ match, onShow }) => {
    if (match.length === 0) {
        return null
    }

    if (match.length === 1) {
        const country = match[0]
        return (
            <section>
                <h2>{country.name}</h2>
                <p>capital: {country.capitals.join(', ')}</p>
                <p>area:     {country.area}</p>
                <h3>languages: </h3>
                <ul>
                    <Languages languages={country.languages} />
                </ul>
                <img src={country.flags.png} alt={country.flags.alt} />
                <Weathers capitals={country.capitals} />
            </section>
        )
    }

    if (match.length > 10) {
        return (
            <section>
                <p>Too many matches, specify another filter</p>
            </section>
        )
    }

    return (
        <section>
            {match.map(x => (
                <p key={x.name}>
                    <span>{x.name} </span>
                    <button onClick={() => onShow(x)}>show</button>
                </p>
            ))}
        </section>
    )

}

export default MatchSection