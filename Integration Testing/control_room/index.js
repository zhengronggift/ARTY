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
    var setPwm = new five.Led(8);
    var setPwm2 = new five.Led(9);
    var setPwm3 = new five.Led(10);
    motors = {
        a: new five.Motor([0, 2, 3]),
        b: new five.Motor([0, 4, 5]),
	c: new five.Motor([0, 6, 7])
    };

    commands = null;
    speed = 255;

    io.on('connection', function (socket) {
        socket.on('stop', function () {
	    speed = 120;
            motors.a.brake();
            motors.b.brake();
            motors.c.brake();
	    setPwm.off();
	    setPwm2.off();
	    setPwm3.off();
        });

        socket.on('start', function () {
            speed = 255;
	    setPwm.on();
	    setPwm2.on();
	    setPwm3.on();
            motors.a.fwd(speed);
            motors.b.fwd(speed);
            motors.c.fwd(speed);
        });

        socket.on('reverse', function () {
            speed = 255;
	    setPwm.on();
	    setPwm2.on();
	    setPwm3.on();
            motors.a.rev(speed);
            motors.b.rev(speed);
            motors.c.rev(speed);
        });

        socket.on('left', function () {
            var aSpeed = 220;
            var bSpeed = 50;
	    setPwm.on();
	    setPwm2.on();
	    setPwm3.on();
            motors.a.fwd(aSpeed);
            motors.b.rev(bSpeed);
            motors.c.fwd(aSpeed);
        });

        socket.on('right', function () {
            var aSpeed = 50;
            var bSpeed = 220;
	    setPwm.on();
	    setPwm2.on();
	    setPwm3.on();
            motors.a.rev(aSpeed);
            motors.b.fwd(bSpeed);
            motors.c.fwd(bSpeed);
        });

        socket.on('audio1', function () {
		var spawn = require("child_process").spawn;  
		var process = spawn('sh',['./publicAudio.sh']);
        });

        socket.on('audio2', function () {
		var spawn = require("child_process").spawn;  
		var process = spawn('sh',['./victimAudio.sh']);
        });
    });
});
