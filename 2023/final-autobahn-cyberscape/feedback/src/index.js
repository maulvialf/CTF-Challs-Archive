const mysql = require('mysql');
const express = require('express');
const session = require('express-session');
const crypto = require('crypto');
const path = require('path');

//etc libs
const fs = require('fs');
const phantom = require('phantom');

const PORT = process.env.PORT || '3000';
const BIND_ADDR = process.env.BIND_ADDR || '0.0.0.0';

const app = express();

const dbpassword = 'REDACTED';

function commentGetConnection(){
	var con = mysql.createConnection({
		host     : '127.0.0.1',
		user     : 'REDACTED',
		password : dbpassword,
		database : 'fakedb'
	});
	return con;
}

app.use(session({
	secret: 'secret',
	resave: false,
	saveUninitialized: true,
	cookie: { httpOnly: false }
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'static')));

app.listen(PORT, BIND_ADDR, () => {
    console.log(`Server listening on ${BIND_ADDR}:${PORT}!`);
});

// http://localhost:3000/
app.get('/', function(request, response) {
	// Render login template
	response.sendFile(path.join(__dirname + '/login.html'));
});

// http://localhost:3000/auth
app.post('/auth', function(request, response) {
	// var initialization
	const now = new Date();
	const unixTime = Math.floor(now.getTime());
	var username = "x";
	var password = "x";
	var clientTime = 0;

	// Capture the input fields
	if (request.body.username) {username = request.body.username;}
	if (request.body.password) {password = request.body.password;}
	if (request.body.token){
		let token = request.body.token;
		var strb64 = Buffer.from(token, 'hex').toString();
		var str = Buffer.from(strb64, 'base64').toString();
		arr = str.split(":");
		host = arr[1];
		database = arr[2];
		clientTime = arr[3];	
	}
	
	console.log(unixTime - clientTime)
	if ((unixTime - clientTime) > 5000) {
		response.send('Invalid Request!');
		response.end();
	}
	else {
		// check data type to prevent SQLI
		if (typeof username != "string" || typeof password != "string"){
			response.send("Invalid parameters!");
			response.end();
			return;
		}
		// Ensure the input fields exists and are not empty
		if (username && password) {
			connection = mysql.createConnection({
				host     : host,
				user     : 'REDACTED',
				password : dbpassword,
				database : database
			});
			connection.query('SELECT * FROM faketable WHERE fakeuser = ? AND fakepass = ?', [username, password], function(error, results, fields) {
				connection.end(function(err) {
					console.log('Connection closed');
				});
				// If the account exists
				if (typeof results !== 'undefined' && results !== null && results !== '') {
					if ( results.length > 0){
						// Authenticate the user
						request.session.loggedin = true;
						request.session.username = username;
						// Redirect to home page
						response.redirect('/home');
					}
					else {
						response.status(401);
						response.send("Incorrect Username and/or Password!");
					}
				} else {
					var resp = "Incorrect Username and/or Password!";
					
					// If there is an issue with the query, output the error
					if (error){
						console.log(error);
						resp = "Error!";
						//resp = error;
					}
					response.status(401);
					response.send(resp);
				}
				response.end();
			});
		} else {
			response.status(401);
			response.send('Please enter Username and Password!');
			response.end();
		}
	}
});

// http://localhost:3000/home
app.get('/home', function(request, response) {
	// If the user is loggedin
	if (request.session.loggedin) {
		response.sendFile(path.join(__dirname + '/commentsection.html'));
	} else {
		// Not logged in
		response.send('Please login to view this page!');
	}
});

// http://localhost:3000/query
app.get('/query', function(request, response) {
	if (request.session.loggedin) {
		response.statusCode == 200;
		response.setHeader('Content-Type', 'text/html');

		var conn = commentGetConnection();

		conn.query('SELECT * FROM comments', function(error, results, fields){
			if(error) throw error;
			
			var comments = JSON.stringify(results);
			response.end(comments);
		});

		conn.end(); 
	} else {
		// Not logged in
		response.send('Please login to view this page!');
	}
});

// http://localhost:3000/insert
app.post('/insert', function(request, response) {
	if (request.session.loggedin) {
		response.statusCode = 200;
		response.setHeader('Content-Type', 'text/plain');

		let name = request.body.name;
		let message = request.body.message;

		var conn = commentGetConnection();
		conn.query('INSERT INTO comments (user, comment) VALUES (?,?)',[name,message], function(error, results, fields){
		if(error) throw error;

		conn.end();
		response.send("Success!");
		});
	} else {
		// Not logged in
		response.send('Please login to view this page!');
	}
});

// FLAG HERE
// http://localhost:3000/admin
app.get('/admin', function(request, response) {
	// If the user is loggedin and admin
	if (request.session.username){
		hashcheck = crypto.createHash('md5').update(request.session.username).digest('hex');
		if (hashcheck == "00000000000000000000000000000000") {
			var flag = fs.readFileSync('flag.txt', 'utf8').trim();
			response.send('Here is your flag: ' + flag );
		}
		else {
			// Not admin
			response.status(403).send('Forbidden');
		}
	}
	else {
		// Not logged in
		response.status(403).send('Forbidden');
	}
	//response.end();
});