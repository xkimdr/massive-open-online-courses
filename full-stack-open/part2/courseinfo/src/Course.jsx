const Header = ({ name }) => <h2>{name}</h2>

const Part = ({ part }) => <p>{part.name} {part.exercises}</p>

const Content = ({ parts }) => <> {parts.map(part => <Part key={part.id} part={part} />)}</>

const Total = ({ sum }) => <p><b>total of {sum} exercises</b></p>

const Course = ({ course }) => {
    return (
        <div>
            <Header name={course.name} />
            <Content parts={course.parts} />
            <Total sum={course.parts.reduce((sum, x) => sum + x.exercises, 0)} />
        </div>
    )
}

export default Course