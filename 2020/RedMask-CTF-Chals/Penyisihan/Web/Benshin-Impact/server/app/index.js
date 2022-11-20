const express = require('express')
const app = express()
const port = 3000

const cookieParser = require('cookie-parser');
app.use(cookieParser());

require('dotenv').config()

const seedrandom = require('seedrandom')

app.set('view engine', 'ejs')
app.use('/static',express.static(__dirname + '/public'))

const firebaseConfig = require('./firebase-config')

const firebase = require('firebase')
firebase.initializeApp(firebaseConfig)

const db = firebase.firestore();

function makeid(length) {
    var result           = ''
    var characters       = '0123456789'
    var charactersLength = characters.length
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength))
    }
    return result
}

app.get('/', (req, res) => {
    let uid;
    if (req.cookies.uid == null) {
        uid = makeid(10)
        res.cookie('uid', uid)
        req.cookies.uid = uid
    } else {
        uid = req.cookies.uid
    }

    res.render('index', {
        uid: uid
    })
})

app.get('/gacha', async (req, res, next) => {
    let uid = req.cookies.uid
    if (uid == null) {
        res.send('no uid')
    }

    let seed;
    let rng;
    try {
        seed = eval('Date.now() + ' + uid)
        rng = seedrandom(seed)
    } catch (e) {
        next(e)
    }

    let num = rng()

    let star = 3
    if (num < 0.05) {
        star = 5
    } else if (num < 0.25) {
        star = 4
    }

    const usersRef = db.collection('users')
    let userQueryRef = await usersRef.doc(Buffer.from(uid).toString('base64')).get()
    if (!userQueryRef.exists) {
        const createUserRef = await db.collection('users').doc(Buffer.from(uid).toString('base64'))
        createUserRef.set({
            'pity': 0,
            'characters': []
        })
        userQueryRef = await usersRef.doc(Buffer.from(uid).toString('base64')).get()
    }
    
    if (userQueryRef.data().pity >= 20) {
        star = 5
    }

    const charactersRef = db.collection('characters')
    const charactersQueryRef = await charactersRef.where('star', '==', star).get()

    const characters = []
    charactersQueryRef.forEach(doc => {
        characters.push(doc.data())
    })

    const charaLength = characters.length
    const charaIndex = Math.floor(Math.random() * Math.floor(charaLength))
    const selectedChara = characters[charaIndex]

    const userRef = usersRef.doc(Buffer.from(uid).toString('base64'))
    let pity
    if (star == 5) {
        pity = 0
    } else {
        pity = firebase.firestore.FieldValue.increment(1)
    }
    let userCharaUnion = await userRef.update({
        characters: firebase.firestore.FieldValue.arrayUnion(selectedChara),
        pity: pity
    })

    res.render('result', {
        name: selectedChara.name
    })
})


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})