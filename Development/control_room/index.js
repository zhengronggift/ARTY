var express = require('express');
var app = express();
var io = require('socket.io')(app.listen(8000));

//Setting the path to static assets
app.use(express.static(__dirname + '/app'));

//Serving the static HTML file
app.get('/', function (res) {
    res.sendFile('/index.html');
});

