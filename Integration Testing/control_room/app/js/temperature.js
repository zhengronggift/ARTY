var myVar3 = setInterval(myTimer3, 1000);

function myTimer3() {
var tempFile = new XMLHttpRequest();
tempFile.open("GET", "/data/temperature.txt", true);

tempFile.onreadystatechange = function () {
    if (tempFile.readyState === tempFile.DONE && (tempFile.status == 200 || tempFile.status == 0) ) {
        allText = tempFile.responseText;
        document.getElementById('temp').innerHTML = allText + "°C";
    }
    //console.log("inside function" + txtFile.responseText);
}
tempFile.send(null);
}
