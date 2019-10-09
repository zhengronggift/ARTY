const express = require('express');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get('/', function(req, res) {
    res.render('index.ejs');
});

/*All static files are in the public, means image, jpg, etc*/
app.use(express.static(__dirname+'/public'));


const server = http.listen(8080, function() {
    console.log('listening on *:8080');
});
