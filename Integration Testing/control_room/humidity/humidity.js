var sensor = require("node-dht-sensor");
var fs = require("fs");
var path = require('path');

var tempPath = path.join(__dirname, '..', 'app', 'temperature.txt');
var humPath = path.join(__dirname, '..', 'app', 'humidity.txt');

sensor.read(11, 4, function(err, temperature, humidity) {
  if (!err) {
    console.log(`temp: ${temperature}°C, humidity: ${humidity}%`);
    fs.writeFile(tempPath, temperature, function (err) {
	if (err) throw err;
	console.log("Temperature Saved!");
	});
    fs.writeFile(humPath, humidity, function (err) {
	if (err) throw err;
	console.log("Humidity Saved!");
	});
  }
});

