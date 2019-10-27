var myVar = setInterval(myTimer, 1000);

function myTimer() {
var humidFile = new XMLHttpRequest();
humidFile.open("GET", "/data/humidity.txt", true);

humidFile.onreadystatechange = function () {
    if (humidFile.readyState === humidFile.DONE && (humidFile.status == 200 || humidFile.status == 0) ) {
        allText = humidFile.responseText;
        document.getElementById('humid').innerHTML = allText + "%";
    }
    //console.log("inside function" + txtFile.responseText);
}
humidFile.send(null);
}

