const bot              = require('../bot');
const express          = require('express');
const router           = express.Router();
const { graphqlHTTP }  = require('express-graphql');
const { execSync }     = require('child_process');
const { existsSync }   = require('fs');
const AuthMiddleware   = require('../middleware/AuthMiddleware');
const GraphqlSchema    = require('../helpers/GraphqlHelper');
const Joi              = require('joi');
const FilterHelper     = require('../helpers/FilterHelper');

let adminReviewing = false;

const response = data => ({ message: data });

router.use('/graphql', AuthMiddleware, graphqlHTTP((req, res) => {
    return {
        schema: GraphqlSchema,
        graphiql: false,
        context: {req, res}
    }
}));

router.get('/', async (req, res) => {
    products = await db.getPotions();

    return res.render('index.html', {products});
});

router.get('/products/:id', async (req, res) => {
    const { id } = req.params;

    product = await db.getPotionByID(id);

    if ( !product.id || product.product_approved == 0) return res.redirect('/');

    let meta = FilterHelper.generateMeta(
        product.product_og_title,
        product.product_og_desc,
        product.product_keywords
    );

    return res.render('product.html', {meta, product});
});

router.get('/login', (req, res) => {
    return res.render('login.html');
});

router.get('/2fa', AuthMiddleware, async (req, res, next) => {
    return res.render('2fa.html', {user: req.user});
});

router.get('/dashboard', AuthMiddleware, async (req, res, next) => {
    products = await db.getPotionsByUser(req.user.username);

    return res.render('dashboard.html', {user: req.user, products});
});

router.post('/api/products/add', AuthMiddleware, async (req, res) => {

    if (adminReviewing) return res.status(500).send('Rate limited!');

    const schema = Joi.object({
        product_name: Joi.string().required(),
        product_desc: Joi.string().required(),
        product_price: Joi.number().required(),
        product_category: Joi.number().min(1).max(100).required(),
        product_keywords: Joi.string().required(),
        product_og_title: Joi.string().required(),
        product_og_desc: Joi.string().required()
    });

    const { error, value } = schema.validate(req.body);
    if (error) {
        return res.status(500).send(response(error.message));
    }

    value.product_desc = FilterHelper.filterHTML(value.product_desc);
    value.product_seller = req.user.username;
    value.product_approved = 0;

    try {
        await db.addPotion(value);
    }
    catch (e) {
        console.log(e)
        return res.status(500).send(response('Something went wrong!'));
    }

    let potion = await db.getAddedPotionID(req.user.username);

    try {
        adminReviewing = true;
        await bot.previewProduct(potion.id);
        adminReviewing = false;
        return res.send(response('Potion added and being reviewed by admin!'));
    }
    catch(e) {
        console.log(e);
        adminReviewing = false;
        return res.status(500).send(response('Something went wrong'));
    }

});

router.get('/products/preview/:id', async (req, res) => {
    const { id } = req.params;

    product = await db.getPotionByID(id);

    if ( !product.id ) return res.redirect('/');

    let meta = FilterHelper.generateMeta(
        product.product_og_title,
        product.product_og_desc,
        product.product_keywords
    );

    return res.render('product.html', {meta, product});
});

router.get('/logout', (req, res) => {
    res.clearCookie('session');
    return res.redirect('/');
});

module.exports = () => {
    return router;
};