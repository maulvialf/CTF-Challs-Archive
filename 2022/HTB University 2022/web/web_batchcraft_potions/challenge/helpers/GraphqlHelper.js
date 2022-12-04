const JWTHelper = require('./JWTHelper');
const OTPHelper = require('./OTPHelper');
const {
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLNonNull,
    GraphQLString,
    GraphQLError
} = require('graphql');

const ResponseType = new GraphQLObjectType({
    name: 'Response',
    fields: {
        message:         { type: GraphQLString },
        token:           { type: GraphQLString }
    }
});

const queryType = new GraphQLObjectType({
    name: 'Query',
    fields: {
        _dummy: { type: GraphQLString }
    }
});

const mutationType = new GraphQLObjectType({
    name: 'Mutation',
    fields: {
        LoginUser: {
            type: ResponseType,
            args: {
                username: { type: new GraphQLNonNull(GraphQLString) },
                password: { type: new GraphQLNonNull(GraphQLString) }
            },
            resolve: async (root, args, {req, res}) => {
                return new Promise((resolve, reject) => {
                    db.loginUser(args.username, args.password)
                        .then(async (user) => {
                            if (user.length) {
                                let token = await JWTHelper.sign({
                                    username: user[0].username,
                                    verified: false
                                });
                                res.cookie('session', token, { maxAge: 3600000 });
                                resolve({
                                    message: "User logged in successfully!",
                                    token: token
                                });
                            };
                            reject(new Error("Username or password is invalid!"));
                        })
                        .catch(err => reject(new GraphQLError(err)));
                });
            }
        },
        verify2FA: {
            type: ResponseType,
            args: {
                otp: { type: new GraphQLNonNull(GraphQLString) }
            },
            resolve: async (root, args, {req, res}) => {
                if (!req.user) return reject(new GraphQLError('Authentication required!'));

                return new Promise(async (resolve, reject) => {
                    secret = await db.getOTPKey(req.user.username);

                    if (await OTPHelper.verifyOTP(secret.otpkey, args.otp)) {
                        let token = await JWTHelper.sign({
                            username: req.user.username,
                            verified: true
                        });
                        res.cookie('session', token, { maxAge: 3600000 });
                        resolve({
                            message: "2FA verified successfully!",
                            token: token
                        });
                    }
                    else {
                        reject(new GraphQLError(new Error('Invalid OTP supplied!')));
                    }
                });
            }
        }
    }
});

module.exports = new GraphQLSchema({
    query: queryType,
    mutation: mutationType
});
