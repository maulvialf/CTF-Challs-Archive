var fs = require('fs');
var express = require('express');
var router = express.Router();
var jwt = require('jsonwebtoken');

var publicKey = fs.readFileSync('./public/key/public.key', 'utf-8');

var verifyOptions = {
    issuer:  'JOINTS21',
    subject:  'ctf@joints.id',
    audience:  'https://joints.id',
    expiresIn:  "12h",
    algorithm:  ["RS256"]
}

router.get('/', function (req, res, next) {
    var token = req.cookies['token']
    if(token === '' || token === undefined)
        res.sendFile('forbidden.html', {root : __dirname + '/../public'});
    else{
        var verify = jwt.verify(token, publicKey,verifyOptions)
        if(verify.admin)
            res.sendFile('flag.html', {root : __dirname + '/'})
        else
            res.sendFile('forbidden.html', {root : __dirname + '/../public'});
    }
})

module.exports = router