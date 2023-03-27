const express = require('express');
const app = express();
const cookiep = require("cookie-parser");
const path = require('path');
const { v4: uuidv4 } = require('uuid');
const redis = require('redis')
const port = process.env.SERVER_PORT;

const BANNED = ['banned list on server! I don\'t want to spoil the chall!'];



const client = redis.createClient({
  'url':process.env.REDIS_URL
})

client.on('error', err => console.log('Redis Client Error', err));
client.connect()

let adminLibs = {};

adminLibs[process.env.ADMIN_ACCOUNT] = {
  "code":`/*
    !!! The best code ever !!!
  */ 
  console.log(1+2);//I think this should output 5
  console.log(flag);//this is my awesome flag`,
  "js-on":{'var_flag':process.env.FLAG}
}


app.use(cookiep());
app.use('/static', express.static('public'))

app.get('/', async (req, res) => {
  let uid = req.cookies.user ? req.cookies.user : '';
  let user = await client.get(uid);
  if(!user){
    uid = uuidv4();
    await client.set(uid,JSON.stringify({
      "code":"console.log(message)",
      "js-on":{'var_message':'Hello World'}
    }))
    res.set({'Set-Cookie':`user=${uid}`});
  }
  res.redirect(`/user/${uid}`);
})

app.get('/code/admin',(req,res)=>{
  let cookie = req.cookies.user;
  if(cookie && cookie === process.env.ADMIN_ACCOUNT){
    return res.json(adminLibs[cookie]);
  }
  res.json({'error':'Did not recieve admin cookie'})
})

app.get('/user/:id',async (req,res)=>{
  let uid = req.params.id ? req.params.id : '';

  let user = await client.get(req.params.id);
  if(!user){
    return res.redirect('/');
  }
  res.sendFile(path.join(__dirname,'public/html/index.html'))
})

app.get('/code/:id',async (req,res)=>{
  let uid = req.params.id; 
  let user = await client.get(uid)
  if(!user){
    return res.json({'error':'Could not find js-on for this'})
  }
  res.json(JSON.parse(user))
})

app.use(express.json());

function checkObjectForBannedKeys(obj) {
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      let keywords = key.split('_');
      if (BANNED.includes(keywords[1].toLowerCase())) {
        return false;
      }
      if (typeof obj[key] === "object" && !Array.isArray(obj[key])) {
        if (!checkObjectForBannedKeys(obj[key])) {
          return false;
        }
      }
    }
  }
  return true;
}

app.post('/code',async (req,res)=>{
  let uid = req.cookies.user ? req.cookies.user : '';
  let user = await client.get(uid);
  if(!user){
    return res.json({'error':'Could not find js-on for that user!'});
  }
  try{
    req.body['js-on'] = JSON.parse(req.body['js-on']);
  }
  catch(e){
    return res.json({'error':'Failed to parse js-on!'})
  }
  console.log(checkObjectForBannedKeys(req.body['js-on']))
  if(checkObjectForBannedKeys(req.body['js-on'])){
    await client.set(req.cookies.user,JSON.stringify(req.body));
    res.json({'success':'JS-ON loaded onto server!'});
  }
  else{
    res.json({'error':'BANNED WORDS DETECTED!'});
  }
})

app.listen(port, () => {
  console.log(`JS-ON available on ${port}`);
})
