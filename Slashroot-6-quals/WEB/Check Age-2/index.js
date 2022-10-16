import express from "express";
import ejs from "ejs";
import path from 'path';
import jwt from 'jsonwebtoken'
import cookieParser from "cookie-parser";
import { fileURLToPath } from "url";
import { v4 as uuidv4 } from 'uuid';

const app = express();
const __dirname = path.dirname(fileURLToPath(import.meta.url));
app.use(express.static(__dirname + "/public"));
app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(cookieParser());

let publicKey = Date.now();
let secret = '';
let s = []

app.use((req,res,next) => {		
	if(!req.cookies?.token){		
		let id = uuidv4()
		let privateKey = Date.now();
		secret = (publicKey + privateKey).toString()
		let token = jwt.sign({ name: 'guess', id }, secret);
		res.cookie('token',token);
		try{
			s.push({secret,id})
		}catch(err){
			s = []
		}
		secret = ''
		next()
	}
	next();
})

app.get("/", async (req, res) => {
	if(req.cookies?.token){
		let tmp = jwt.decode(req.cookies.token)
		if(tmp?.id){
			let secret = s.filter(e => e.id === tmp.id)[0]
			if(secret?.secret){
				try{
					let decoded = jwt.verify(req.cookies.token,secret.secret)
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
					const security = (cc) => cc.match(/^.*(global|this|process|eval|object|charAt|-|_|{|}|function).*$/i) || cc.length > 100
					if(yearOfBirth || yearOfBirth == ''){
						if(!parseInt(yearOfBirth)){
							return res.status(405).send(err)
						}
					}
					if(security(decoded.name)){
						console.log("kena", decoded.name)
						return res.status(405).send(err);
					}

					let template = ejs.compile(`
						<!DOCTYPE html>
						<html lang="en">
						<head>
							<meta charset="UTF-8">
							<meta http-equiv="X-UA-Compatible" content="IE=edge">
							<meta name="viewport" content="width=device-width, initial-scale=1.0">
							<link rel="stylesheet" href="css/styles.css">
							<title>Check Age 2</title>
						</head>
						<body>    
						<div class="h-100 p-20 w-full flex flex-col items-center justify-center font-sans">    
							<h1 class="text-5xl font-bold text-blue-400 mb-4">Check Age 2!</h1>
							<form action="/" method="get">            
								<input placeholder='Year of Birth' min="1000" class='border-2 rounded-sm shadow-sm px-2 py-1 focus:outline-none focus:border-blue-400' type="number" name="yearOfBirth" id="yearOfBirth">
								<button class='border-2 px-4 active:bg-blue-300 active:text-white rounded-sm shadow-sm py-1' type="submit">Check</button>
							</form>

							<% if(${(yearOfBirth) ? yearOfBirth : 0}) { %>							
								<% if(${yearOfBirth} < 0 || ${yearOfBirth} >= 9999){ %>
									<h5 class='pt-1 text-green-400'>Hmmm... are you human?</h5>
								<%}else {%>
									<h5 class='pt-1 text-green-400'>${decoded.name} your age is <%= new Date().getFullYear() - ${(yearOfBirth) ? yearOfBirth : 0} %> Years Old</h5>
								<% } %>
							<% } %>
						</div>
						</body>
						</html>
					`);
					return res.send(template());
					

				}catch(err){
					console.log(err)
					return res.send('Something wrong')
				}

			}
			return res.send("Delete your token!")
		}
		
	}
	return res.send("Please refresh again!")
    
});

app.listen(20201);