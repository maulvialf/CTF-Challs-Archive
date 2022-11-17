const express        = require('express');
const router         = express.Router();
const JWTHelper      = require('../helpers/JWTHelper');
const AuthMiddleware = require('../middleware/AuthMiddleware');


let db;

const response = data => ({ message: data });

router.get('/', (req, res) => {
	return res.render('login.html');
});

router.get('/register', (req, res) => {
	return res.render('register.html');
});

router.post('/api/register', async (req, res) => {

	const { username, password, email } = req.body;

	if (username && password && email) {
		return db.checkUser(username)
			.then(user => {
				if (user) return res.status(401).send(response('User already registered!'));
				db.getLastUuid()
					.then(uuid => {
						return db.registerUser(username, password, email, uuid.uuid + 1)
							.then(() => res.send(response('User registered successfully!')))
					})
			})
			.catch(() => res.send(response('Something went wrong!')));
	}
	return res.status(401).send(response('Please fill out all the required fields!'));
});

router.post('/api/login', async (req, res) => {

	const { username, password } = req.body;

	if (username && password) {
		return db.loginUser(username, password)
			.then(user => {
				let token = JWTHelper.sign({ username: user.username });
				res.cookie('session', token, { maxAge: 3600000 });
				res.send(response('User authenticated successfully!'));
			})
			.catch(() => res.status(403).send(response('Invalid username or password!')));
	}
	return res.status(500).send(response('Missing parameters!'));
});

router.get('/dashboard', AuthMiddleware, async (req, res, next) => {

	return db.getUser(req.data.username)
		.then(user => {
			if (user === undefined) return res.redirect('/');
			res.render('dashboard.html', {user});
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.get('/api/passwords/:uuid', AuthMiddleware, async (req, res) => {

	return db.getUser(req.data.username)
		.then(user => {
			if (user === undefined) return res.redirect('/'); 
			if (req.params.uuid) {
				return db.getSavedPasswords(req.params.uuid)
					.then(passwords  => {
						if(passwords) return res.send({passwords});
						res.status(404).send(response('user does not exist'));
				})	
			}
			return res.status(403).send(response('Missing parameters!'));
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.post('/api/passwords/add', AuthMiddleware, async (req, res) => {

	return db.getUser(req.data.username)
		.then(user => {
			if (user === undefined) return res.redirect('/'); 
			const { recType, recAddr, recUser, recPass, recNote } = req.body;
			if (recType && recAddr && recUser && recPass && recNote) {
				return db.addPassword(user.uuid, recType, recAddr, recUser, recPass, recNote)
					.then(()  => res.send(response('Password added successfully!')))	
			}
			return res.status(403).send(response('Missing parameters!'));
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.post('/api/passwords/delete', AuthMiddleware, async (req, res) => {

	return db.getUser(req.data.username)
		.then(user => {
			if (user === undefined) return res.redirect('/'); 
			const { passId } = req.body;
			if (passId) {
				return db.delPassword(user.uuid, passId)
					.then(()  => res.send(response('Password deleted successfully!')))	
			}
			return res.status(403).send(response('Missing parameters!'));
		})
		.catch(() => res.status(500).send(response('Something went wrong!')));
});

router.get('/logout', (req, res) => {
	res.clearCookie('session');
	return res.redirect('/');
});

module.exports = database => { 
	db = database;
	return router;
};