const puppeteer = require('puppeteer');
const JWTHelper = require('./helpers/JWTHelper');
const fs        = require('fs');

const flag = fs.readFileSync('/flag.txt').toString();

const browser_options = {
    headless: true,
    executablePath: '/usr/bin/chromium-browser',
    args: [
        '--no-sandbox',
        '--disable-background-networking',
        '--disable-default-apps',
        '--disable-extensions',
        '--disable-gpu',
        '--disable-sync',
        '--disable-translate',
        '--hide-scrollbars',
        '--metrics-recording-only',
        '--mute-audio',
        '--no-first-run',
        '--safebrowsing-disable-auto-update',
        '--js-flags=--noexpose_wasm,--jitless'
    ]
};

const previewProduct = async (id) => {
    const browser = await puppeteer.launch(browser_options);

    try {
        let context = await browser.createIncognitoBrowserContext();
        let page = await context.newPage();

        let token = await JWTHelper.sign({ username: 'admin', verified: true, flag: flag });

        await page.setCookie({
            name: "session",
            value: token,
            domain: "127.0.0.1"
        });

        await Promise.race(
            [
                page.goto(`http://127.0.0.1/products/preview/${id}`, {
                    waitUntil: 'networkidle2'
                }),
                new Promise(function (reject) {
                    setTimeout(function (){
                        reject();
                    }, 7000);
                }),
            ]
        );
    }
    finally {
        await browser.close();
    }
};

module.exports = { previewProduct };