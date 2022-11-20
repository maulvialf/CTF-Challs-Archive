var fs = require('fs');
var express = require('express');
var router = express.Router();
var jwt = require('jsonwebtoken');

var privateKey = fs.readFileSync('./public/key/private.key', 'utf-8');
var publicKey = fs.readFileSync('./public/key/public.key', 'utf-8');

var signOptions = {
  issuer:  'JOINTS21',
  subject:  'ctf@joints.id',
  audience:  'https://joints.id',
  expiresIn:  "12h",
  algorithm:  "RS256"
}

var verifyOptions = {
  issuer:  'JOINTS21',
  subject:  'ctf@joints.id',
  audience:  'https://joints.id',
  expiresIn:  "12h",
  algorithm:  ["RS256"]
}

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index.html');
});

router.get('/auth', function (req, res, next) {
  var token = req.cookies['token']
  if(token === '' || token=== undefined){
    var randName = 'guest' + Math.round(Math.random()*1000);
    var token = jwt.sign({ name: randName, admin:false },privateKey,signOptions);

    res.cookie('token', token);
    res.send()
  }
  else
    res.send('ok');
});


router.get('/verify', function (req, res, next) {
  var token = req.cookies['token']
  // console.log(token)
  var verify = jwt.verify(token, publicKey,verifyOptions)
  res.send(verify)
})

module.exports = router;
