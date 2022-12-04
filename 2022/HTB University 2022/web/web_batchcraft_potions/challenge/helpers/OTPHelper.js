const { authenticator } = require('@otplib/preset-default');
const qrcode            = require('qrcode');

authenticator.options = { digits: 4 };

const genSecret = () => {
    return authenticator.generateSecret();
}

const genPin = (secret) => {
    return authenticator.generate(secret);
}

const genQRcode = async (username, secret) => {
    return new Promise(async (resolve, reject) => {
        const otpauth = authenticator.keyuri(username, 'Genesis', secret);
        qrcode.toDataURL(otpauth, (err, imageUrl) => {
            if (err) reject(err);
            resolve(imageUrl);
        });
    });
}

const verifyOTP = async (otpkey, otp) => {
    return new Promise(async (resolve, reject) => {
        try {
            isValid = authenticator.check(otp, otpkey);
            if (isValid) return resolve(true);
            return resolve(false);
        }
        catch (err) {
            resolve(false);
        }
    });
}

module.exports = {
	genQRcode,
    genSecret,
    verifyOTP,
    genPin
}