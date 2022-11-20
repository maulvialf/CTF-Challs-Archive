// ./node_modules/pkg/lib-es5/bin.js .
const prompt = require('prompt-sync')()

const process = (something) => {
    let result = 'J'
    for (let i = 1; i < something.length; i+=1) {
        result += String.fromCharCode(something.charCodeAt(i) ^ something.charCodeAt(i-1))
    }
    return result
}

const main = () => {
    const what = 'JNKMPV46s<b?ahQ`~N\x7f KsyEGt.p-sy@D\x10q|S@\x17uLvIC\x18ABJ^V\x01N'
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