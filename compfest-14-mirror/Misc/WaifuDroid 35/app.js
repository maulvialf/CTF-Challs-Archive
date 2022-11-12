const Discord = require(`discord.js`);
const client = new Discord.Client();

const { secret } = require(`./secrets.js`);

const responses = {
    reticent: [`Grrr`, `NO FLAG`, `No flag!`, `Нет флага`, `\u{1F47A}`, `ｎｏ　ｆｌａｇ`,  `Ora ana bendera`, `Teu aya bendera`],
    secret: secret
};

const isValid = (str) => {
    let allowedChars = [`+`,`-`,`/`,`~`,`[`,`]`,`{`,`}`,`!`];
	for(let chr of str) {
		if(!allowedChars.includes(chr)) return false;
	}
	return true;
};

const fetchResponse = (responseType) => {
    return responses[responseType][Math.floor(Math.random() * responses[responseType].length)];
};

client.on(`message`, (msg) => {
    let user = msg.author;
    if(msg.channel.type != `dm` || user == client.user) return;
    let content = msg.content;
	
	let response = fetchResponse(`reticent`);
	
	if(content.length > 766 || !isValid(content)) {
		return user.send(response);
	}
	
    try {
        content = eval(content);
    } catch(err) {
        content = ``;
    }
	
	if(content === `yes Flag`) {
		response = fetchResponse(`secret`);
	}
	
	user.send(response);
});

client.login(process.env.BOT_TOKEN);
