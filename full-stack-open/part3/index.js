require("dotenv").config();
const express = require("express");
const morgan = require("morgan");
const Person = require("./models/person");

const app = express();

app.use(express.static("dist"));
app.use(express.json());

morgan.token("body", (req) => JSON.stringify(req.body));
app.use(morgan(":method :url :status :res[content-length] - :response-time ms :body"));

app.get("/api/people", (req, res, next) => {
    Person
        .find({})
        .then(p => res.json(p))
        .catch(e => next(e));
});

app.get("/api/people/:id", (req, res, next) => {
    Person
        .findById(req.params.id)
        .then(p => {
            if (p) {
                res.json(p);
            } else {
                res.status(400).end();
            }
        })
        .catch(e => next(e));
});

app.get("/info", (req, res, next) => {
    Person
        .countDocuments({})
        .then(n => {
            const body = [
                `<p>Phonebook has info for ${n} people</p>`,
                `<p>${new Date().toString()}</p>`,
            ].join("\n");

            res.send(body);
        })
        .catch(e => next(e));
});

app.post("/api/people", (req, res, next) => {
    const body = req.body;

    if (!body.name || !body.number) {
        return res.status(404).json({
            error: "content missing",
        });
    }

    Person
        .countDocuments({ name: body.name })
        .then(n => {
            if (n !== 0) {
                return res
                    .status(404)
                    .json(
                        { error: "name must be unique" }
                    );
            }

            const person = new Person({
                name: body.name,
                number: body.number,
            });

            person
                .save()
                .then(p => res.json(p))
                .catch(e => next(e));
        })
        .catch(e => next(e));
});


app.delete("/api/people/:id", (req, res, next) => {
    Person
        .findByIdAndDelete(req.params.id)
        .then(() => res.status(204).end())
        .catch(e => next(e));
});

app.put("/api/people/:id", (req, res, next) => {
    Person
        .findByIdAndUpdate(
            req.params.id,
            {
                name: req.body.name,
                number: req.body.number,
            },
            {
                new: true,
                runValidators: true,
                context: "query"
            }
        )
        .then(p => {
            if (p) {
                res.json(p);
            } else {
                res.status(400).send({ error: `${req.body.name} no longer exist` });
            }
        })
        .catch(e => next(e));
});

const unknownEndpoint = (req, res) => {
    res.status(404).send({ error: "unknown endpoint" });
};

app.use(unknownEndpoint);

const errorHandler = (e, req, res, next) => {
    console.error(e.message);

    if (e.name === "CastError") {
        return res.status(400).send({ error: "malformatted id" });
    } else if (e.name === "ValidationError") {
        return res.status(400).json({ error: e.message });
    }

    next(e);
};

app.use(errorHandler);

const PORT = process.env.PORT;
app.listen(PORT, () => console.log(`Server started at ${PORT}`));
