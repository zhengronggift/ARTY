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
        a: new five.Motor([4, 5, 6]),
        b: new five.Motor([7, 8, 9]),
	c: new five.Motor([10, 11, 12])
    };

    commands = null;
    speed = 255;

    io.on('connection', function (socket) {
        socket.on('stop', function () {
	    speed = 120;
            motors.a.brake();
            motors.b.brake();
            motors.c.brake();
        });

        socket.on('start', function () {
            speed = 255;
            motors.a.fwd(speed);
            motors.b.fwd(speed);
            motors.c.fwd(speed);
        });

        socket.on('reverse', function () {
            speed = 255;
            motors.a.rev(speed);
            motors.b.rev(speed);
            motors.c.rev(speed);
        });

        socket.on('left', function () {
            var aSpeed = 220;
            var bSpeed = 50;
            motors.a.fwd(aSpeed);
            motors.b.rev(bSpeed);
            motors.c.fwd(aSpeed);
        });

        socket.on('right', function () {
            var aSpeed = 50;
            var bSpeed = 220;
            motors.a.rev(aSpeed);
            motors.b.fwd(bSpeed);
            motors.c.fwd(bSpeed);
        });
    });
});
