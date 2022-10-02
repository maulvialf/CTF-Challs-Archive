
let express = require('express')
let ejs = require('ejs');
let jwt = require('jsonwebtoken');
let cookieParser = require('cookie-parser');

const app = express();

app.use(express.static(__dirname + "/public"));
app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(cookieParser());

let secret = Date.now();
console.log(secret)
app.use((_,res,next) => {		
	let token = jwt.sign({ name: 'guess'}, secret.toString());
	res.cookie('token',token);
	next();
})

app.get("/", (req, res) => {
	if(req.cookies?.token){
		try{
			let decoded = jwt.verify(req.cookies.token,secret.toString());
			let err = ejs.render(`
				<!DOCTYPE html>
				<html lang="en">
				<head>
					<meta charset="UTF-8">
					<meta http-equiv="X-UA-Compatible" content="IE=edge">
					<meta name="viewport" content="width=device-width, initial-scale=1.0">
					<link rel="stylesheet" href="css/styles.css">
					<title>Error</title>
				</head>
				<body>    
				<div class="h-screen w-full bg-blue-100 flex flex-col p-5 items-center justify-center font-sans">    
					<div>
						<h1 class="text-center text-4xl text-blue-300"> Not Allowed </h1>
					</div>
				</div>
				</body>
				</html>
			`)
			const { yearOfBirth } = req.query;

			if(yearOfBirth || yearOfBirth == ''){
				if(!parseInt(yearOfBirth)){
					return res.status(405).send(err)
				}
			}

			let template = ejs.compile(`
				<!DOCTYPE html>
				<html lang="en">
				<head>
					<meta charset="UTF-8">
					<meta http-equiv="X-UA-Compatible" content="IE=edge">
					<meta name="viewport" content="width=device-width, initial-scale=1.0">
					<link rel="stylesheet" href="css/styles.css">
					<title>Check Age</title>
				</head>
				<body>    
				<div class="h-100 p-20 w-full flex flex-col items-center justify-center font-sans">    
					<h1 class="text-5xl font-bold text-blue-400 mb-4">Check Age!</h1>
					<form action="/" method="get">            
						<input placeholder='Year of Birth' min="1000" class='border-2 rounded-sm shadow-sm px-2 py-1 focus:outline-none focus:border-blue-400' type="number" name="yearOfBirth" id="yearOfBirth">
						<button class='border-2 px-4 active:bg-blue-300 active:text-white rounded-sm shadow-sm py-1' type="submit">Check</button>
					</form>

					<% if(${(yearOfBirth) ? yearOfBirth : 0}) { %>							
						<% if(${yearOfBirth} < 0 || ${yearOfBirth} >= 9999){ %>
							<h5 class='pt-1 text-green-400'>Hmmm... are you human?</h5>
						<%}else {%>
							<h5 class='pt-1 text-green-400'> ${decoded.name} your age is <%= new Date().getFullYear() - ${(yearOfBirth) ? yearOfBirth : 0} %> Years Old</h5>
						<% } %>
					<% } %>
				</div>
				</body>
				</html>
			`);
			return res.send(template());
		}catch(err){
			console.log(err)
			return res.send('Something wrong');
		}
	}
	return res.send('invalid token');
    
});

app.listen(20201);