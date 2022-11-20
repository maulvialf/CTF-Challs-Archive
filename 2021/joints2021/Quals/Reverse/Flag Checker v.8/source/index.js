const prompt = require('prompt-sync')()

const _0x57fe=['length','fromCharCode'];const _0x3a5b=function(_0x1c8847,_0x57fe77){_0x1c8847=_0x1c8847-0x1e2;let _0x3a5bec=_0x57fe[_0x1c8847];return _0x3a5bec;};const process=_0x3f142d=>{const _0x1ea327=_0x3a5b;let _0x1bd392='J';for(let _0x4fefd5=0x1;_0x4fefd5<_0x3f142d[_0x1ea327(0x1e2)];_0x4fefd5+=0x1){_0x1bd392+=String[_0x1ea327(0x1e3)](_0x3f142d['charCodeAt'](_0x4fefd5)^_0x3f142d['charCodeAt'](_0x4fefd5-0x1));}return _0x1bd392;};

const main = () => {
    const what = 'J\x05\x06\x07\x1a\x07a\x03JN]\\Y\x08:0\x0112^l9\t=\r2Y_Z_\t8;Ub\x0c(\x12Tc6;<\x0b\\X\x00\t\x0b\tTN'
    try {
        const inp = prompt('Your Input: ')
        if(inp.length === what.length) {
            if(process(inp) === what) {
                console.log('Yeay')
                return;
            }
        }
        console.log('Yikes')
    } catch (err) {
        console.log('Yikes')
    }
}

module.exports = {
	main
};