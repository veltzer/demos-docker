#!/usr/bin/env node

var http = require('http');
const port = 8000
 
http.createServer(
	function (request, response) {
		response.writeHead(200, {'Content-Type': 'text/plain'});
		response.end('Hello World from node.js\n');
	}
).listen(port);
	 
console.log(`Contact me at http://localhost:${port}`)
