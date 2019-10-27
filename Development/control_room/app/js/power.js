var myVar2 = setInterval(myTimer2, 1000);

function myTimer2() {
var powerFile = new XMLHttpRequest();
powerFile.open("GET", "/data/power.txt", true);

powerFile.onreadystatechange = function () {
    if (powerFile.readyState === powerFile.DONE && (powerFile.status == 200 || powerFile.status == 0) ) {
        allText = powerFile.responseText;
        document.getElementById('power').innerHTML = allText + "%";
        document.getElementById('powerbar').setAttribute("style","width:"+allText+"%");
    }
    //console.log("inside function" + txtFile.responseText);
}
powerFile.send(null);
}
