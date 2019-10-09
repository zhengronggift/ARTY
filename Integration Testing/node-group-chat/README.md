# Build A Group-Chat App in 30 Lines Using Node.js

A simple and (hopefully) to-the-point tutorial to build your first group-chat application using Node.js in less than 30 lines of code.

## Running the program

Run the program by using

```shell
$ node index.js
```

npm init
npm install express
npm install socket.io
npm install ejs

npm i nodemon -g
nodemon server.js

sudo nano /etc/nginx/sites-enabled/default

upstream project {
        server IP&PORT;
	#server IP&PORT;
	#server IP&PORT;
}

server {
        listen 80;
        location / {
                proxy_pass http://project;
        }
}

sudo service nginx start 
sudo service nginx reload

more details:
https://www.youtube.com/watch?v=FJrs0Ar9asY

