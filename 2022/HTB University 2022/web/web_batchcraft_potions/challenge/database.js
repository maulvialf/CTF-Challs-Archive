const mysql     = require('mysql')
const crypto    = require('crypto');
const OTPHelper = require('./helpers/OTPHelper');

class Database {

	constructor() {
		this.connection = mysql.createConnection({
			host: '127.0.0.1',
			user: 'batchcraftpotions',
			password: 'batchcraftpotions',
			database: 'batchcraftpotions'
		});
	}

	async connect() {
		return new Promise((resolve, reject)=> {
			this.connection.connect((err)=> {
				if(err)
					reject(err)
				resolve()
			});
		})
	}

    async migrate() {
		let otpkey = OTPHelper.genSecret();

        let stmt = `INSERT IGNORE INTO users(username, password, otpkey, is_admin) VALUES(?, ?, ?, ?)`;
        this.connection.query(
            stmt,
            [
                'vendor53',
                'PotionsFTW!',
                otpkey,
                0
            ],
            (err, _) => {
                if(err)
                    console.error(err);
            }
        )
	}

    async loginUser(username, password) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT username, otpkey FROM users WHERE username = ? and password = ?`;
			this.connection.query(
                stmt,
                [
                    String(username),
                    String(password)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        resolve(JSON.parse(JSON.stringify(result)))
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async getUser(username) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT * FROM users WHERE username = ?`;
			this.connection.query(
                stmt,
                [
                    String(username)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        resolve(JSON.parse(JSON.stringify(result)))
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async getOTPKey(username) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT otpkey FROM users WHERE username = ?`;
			this.connection.query(
                stmt,
                [
                    String(username)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        let rows = JSON.parse(JSON.stringify(result))
                        resolve(rows.length ? rows[0] : {})
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async getPotions() {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT * FROM products where product_approved = 1`;
			this.connection.query(
                stmt, [],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        resolve(JSON.parse(JSON.stringify(result)))
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async getPotionsByUser(username) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT * FROM products WHERE product_seller = ?`;
			this.connection.query(
                stmt,
                [
                    String(username)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        resolve(JSON.parse(JSON.stringify(result)))
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async getPotionByID(id) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT * FROM products WHERE id = ?`;
			this.connection.query(
                stmt,
                [
                    String(id)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        let rows = JSON.parse(JSON.stringify(result))
                        resolve(rows.length ? rows[0] : {})
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async getAddedPotionID(username) {
		return new Promise(async (resolve, reject) => {
			let stmt = `SELECT id FROM products WHERE product_seller = ? ORDER BY id DESC LIMIT 1`;
			this.connection.query(
                stmt,
                [
                    String(username)
                ],
                (err, result) => {
                    if(err)
                        reject(err)
                    try {
                        let rows = JSON.parse(JSON.stringify(result))
                        resolve(rows.length ? rows[0] : {})
                    }
                    catch (e) {
                        reject(e)
                    }
			    }
            )
		});
	}

    async addPotion(data) {
		return new Promise(async (resolve, reject) => {
			let stmt = `
            INSERT INTO products(
                product_name,
                product_desc,
                product_price,
                product_category,
                product_keywords,
                product_og_title,
                product_og_desc,
                product_seller,
                product_approved
            )
            VALUES (?,?,?,?,?,?,?,?,?)`;

			this.connection.query(
                stmt,
                [
                    data.product_name,
                    data.product_desc,
                    data.product_price,
                    data.product_category,
                    data.product_keywords,
                    data.product_og_title,
                    data.product_og_desc,
                    data.product_seller,
                    data.product_approved
                ],
                (err, _) => {
                    if(err)
                       return reject(err)
                    resolve()
			    }
            )
		});
	}

}

module.exports = Database;