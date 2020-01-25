"use strict";
const http = require('http');
const fs = require('fs');
const path = require('path');
const mime = require('mime');
const net   = require('net');
require('abstractsocket')(net);

const PORT_NUMBER = 8088;
const SOCKET_FILE = '/tmp/q3-mobify';
var stub = net.createConnection(SOCKET_FILE);
stub.on("connect", () => {
	console.log("Connected to backend.");
});

var server = http.createServer(function (request, response) {
	var filePath = false;

	if (request.method == 'POST') {
		console.log('POST')
		var body = ''
		request.on('data', function (data) {
			body += data
			console.log('Partial body: ' + body)
		});
		request.on('end', function () {
			body = body.trim();
			console.log('Body: ' + body)
			stub.on("data", (data) => {
				response.writeHead(200, { 'Content-Type': 'text/plain' });
				response.end(data.toString());
			})
			.on("error", (e)=>{
				console.error(e);
			});
			stub.write(body);
		})
	} else {
		if (request.url == '/?') return;
		if (request.url == '/') {
			filePath = 'public/index.html';
		} else {
			filePath = 'public' + request.url;
		}
	
		var absPath = './' + filePath;
		fs.exists(absPath, function (exists) {
			if (exists) {
				fs.readFile(absPath, function (err, data) {
					if (err) {
						send404(response);
					} else {
						sendFile(response, absPath, data);
					}
				});
			} else {
				send404(response);
			}
		});
	}

});

server.listen(PORT_NUMBER, function () {
	console.log("Server listeneing on port " + PORT_NUMBER);
});

function send404(response) {
	response.writeHead(404, { 'Content-Type': 'text/plain' });
	response.write('Error 404: resource not found.');
	response.end();
}

function sendFile(response, filePath, fileContents) {
	response.writeHead(
		200,
		{ "content-type": mime.getType(path.basename(filePath)) }
	);
	response.end(fileContents);
}
