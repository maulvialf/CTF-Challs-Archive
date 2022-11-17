const JWTHelper = require('../helpers/JWTHelper');

module.exports = async (req, res, next) => {
	try{
		if (req.cookies.session === undefined) {
			if(!req.is('application/json')) return res.redirect('/');
			return res.status(401).json({ message: 'Authentication required!' });
		}
		let data = await JWTHelper.decode(req.cookies.session);
		req.data = {
			username: data.username
		}
		next();
	} catch(e) {
		return res.status(500).send('Internal server error');
	}
}