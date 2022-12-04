const JWTHelper = require('../helpers/JWTHelper');

module.exports = async (req, res, next) => {
	try {
		if (req.cookies.session === undefined) {
            if (req.originalUrl === '/graphql') return next();
			if (!req.is('application/json')) return res.redirect('/');
			return res.status(401).json({ status: 'unauthorized', message: 'Authentication required!' });
		}
		return JWTHelper.verify(req.cookies.session)
			.then(user => {
                req.user = user;

                if (req.originalUrl === '/graphql' || req.originalUrl === '/2fa') return next();
                if (user.verified === false) return res.redirect('/login');

				return next();
			})
			.catch((e) => {
                if (req.originalUrl === '/graphql') return next();
				res.redirect('/logout');
			});
	} catch(e) {
		console.log(e);
		return res.redirect('/logout');
	}
}