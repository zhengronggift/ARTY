var express = require('express');
var app = express();
var io = require('socket.io')(app.listen(8000));
var five = require('johnny-five');

//Setting the path to static assets
app.use(express.static(__dirname + '/app'));

//Serving the static HTML file
app.get('/', function (res) {
    res.sendFile('/index.html')
});

var board = new five.Board({
    repl: false
});

board.on('ready', function () {
    var speed, commands, motors;
    motors = {
        a: new five.Motor([12, 4]),
        b: new five.Motor([13, 5])
    };

    commands = null;
    speed = 255;

    io.on('connection', function (socket) {
        socket.on('stop', function () {
	    speed = 120;
            motors.a.rev(speed);
            motors.b.rev(speed);
        });

        socket.on('start', function () {
            speed = 150;
            motors.a.fwd(speed);
            motors.b.fwd(speed);
        });

        socket.on('reverse', function () {
            speed = 120;
            motors.a.rev(speed);
            motors.b.rev(speed);
        });

        socket.on('left', function () {
            var aSpeed = 220;
            var bSpeed = 50;
            motors.a.fwd(aSpeed);
            motors.b.rev(bSpeed);
        });

        socket.on('right', function () {
            var aSpeed = 50;
            var bSpeed = 220;
            motors.a.rev(aSpeed);
            motors.b.fwd(bSpeed);
        });
    });
});