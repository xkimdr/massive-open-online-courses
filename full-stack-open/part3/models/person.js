const mongoose = require("mongoose");

const URI = process.env.MONGODB_URI;

mongoose
    .connect(URI)
    .then(() => {
        console.log("connected to MongoDB");
    }).catch((error) => {
        console.log("error connecting to MongoDB:", error.message);
    });

const personSchema = new mongoose.Schema({
    name: {
        type: String,
        minLength: 3,
        required: true
    },
    number: {
        type: String,
        minLength: 8,
        required: true,
        validate: {
            validator: v => /^\d{2,3}-\d{5,}$/.test(v),
            message: props => `${props.value} is not a valid phone number!`
        },
    }
});

personSchema.set("toJSON", {
    transform: (document, returnedObject) => {
        returnedObject.id = returnedObject._id.toString();
        delete returnedObject._id;
        delete returnedObject.__v;
    }
});

module.exports = mongoose.model("Person", personSchema);