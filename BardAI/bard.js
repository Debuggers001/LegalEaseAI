const fs = require('fs');
const express = require("express");

const app = express();
const port = 80;

const bard = fs.readFileSync('bard.html')

app.get('/', (req, res) => {
    res.end(bard);
});

app.post('/', (req, res) => {
    
    let name = req.body.name;
    let gender = req.body.gender;
    let age = req.body.age;
    let query = req.body.query;


    let info = `Client name: ${name} \n Gender: ${gender} \n Age: ${age} \n Query: ${query}` 
    fs.writeFileSync('info.txt', info)
    res.end("<h1>Thankyou for submitting</h1>");
});

app.listen(port, () => {
    console.log(`App is running at port ${port}`);
});