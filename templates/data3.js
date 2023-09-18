const fs=require('fs')
const path=require('path')
const express=require('express')
const app=express()
const port= 80
const hostname='127.0.0.2'
//app.get('/',(req,res)=>{
//    res.status(200).sendFile(path.join(__filename,'bard.html'))
//})

app.get('/', (req, res) => {
    // Read the HTML file
    let data1=fs.readFileSync('data3.txt','utf-8')
    fs.readFile('bard.html', 'utf8', (err, data) => {
        if (err) {
            res.status(500).send('Internal Server Error');
            return;
        }
        else{
        // Replace the placeholder in the HTML file with the variable's value
        const updatedData = data.replace('{{draft}}', data1);

        // Send the updated HTML as the response
        res.send(updatedData);
        }
    });
});
app.listen(port, hostname, ()=> {
    console.log(`Server is active at http://${hostname}:${port}`);
});

