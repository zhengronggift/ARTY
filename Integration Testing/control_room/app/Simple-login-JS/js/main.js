function clicked () {
	var user = document.getElementById('username');
	var pass = document.getElementById('password');

	var coruser = 'rong';
	var corpass = 'letmein';

		if(user.value == coruser)  {

			if(pass.value == corpass) {

				window.alert("Hi, Rong " + user.value);
				window.open("http://google.com");

			}  else  {

				window.alert("Sorry, wrong password");

			}

		}  else {

			window.alert("Please enter something");



		}
}

// forza Napoli always :) 
