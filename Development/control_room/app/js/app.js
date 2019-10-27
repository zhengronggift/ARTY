var socket = io();
var x = document.getElementById("myAudio"); 
var x2 = document.getElementById("myAudio2"); 

function stop(){
    socket.emit('stop');
}

function moveForward(){
    socket.emit('start');
}

function turnRight(){
    socket.emit('right');
}

function turnLeft(){
    socket.emit('left');
}

function moveReverse(){
    socket.emit('reverse');
}

function playAudio() { 
  x.play(); 
} 

function playAudio2() { 
  x2.play(); 
} 

function pauseAudio() { 
  x.pause(); 
  x2.pause(); 
} 

document.getElementById('forward').onclick = moveForward;
document.getElementById('right').onclick = turnRight;
document.getElementById('left').onclick = turnLeft;
document.getElementById('reverse').onclick = moveReverse;
document.getElementById('stop').onclick = moveReverse;