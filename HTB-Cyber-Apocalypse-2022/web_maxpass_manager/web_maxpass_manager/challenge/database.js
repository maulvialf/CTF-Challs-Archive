const sqlite = require('sqlite-async');

class Database {
    constructor(db_file) {
        this.db_file = db_file;
        this.db = undefined;
    }
    
    async connect() {
        this.db = await sqlite.open(this.db_file);
    }

    async migrate() {
        return this.db.exec(`
            DROP TABLE IF EXISTS users;

            CREATE TABLE IF NOT EXISTS users (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username   VARCHAR(255) NOT NULL UNIQUE,
                password   VARCHAR(255) NOT NULL,
                email      VARCHAR(255) NOT NULL,
                uuid       INTEGER NOT NULL
            );

            INSERT INTO users (username, password, email, uuid) VALUES ('admin', '[REDACTED SECRET]', 'admin@maxpass-manager.com', 73);
            INSERT INTO users (username, password, email, uuid) VALUES ('louisbarnett', 'mcd0nalds#21', 'louis_p_barnett@mailinator.com', 141);
            INSERT INTO users (username, password, email, uuid) VALUES ('ninaviola', '1katz&2dogz', 'ninaviola57331@mailinator.com', 142);
            INSERT INTO users (username, password, email, uuid) VALUES ('alvinfisher', 'September#2019', 'alvinfisher1979@mailinator.com', 143);

            DROP TABLE IF EXISTS user_data;

            CREATE TABLE IF NOT EXISTS user_data (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                uuid       INTEGER NOT NULL,
                type       VARCHAR(255) NOT NULL,
                address    VARCHAR(255) NOT NULL,
                username   VARCHAR(255) NOT NULL,
                password   VARCHAR(255) NOT NULL,
                note       VARCHAR(255) NOT NULL
            );

            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (73,'Web','maxpass-manager.infra','admin','[REDACTED SECRET]','pre-prod test password');
            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (141,'Web','spotify.com','louisbarnett','YMgC41@)pT+BV','student sub');
            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (141,'Email','protonmail.com','louisbarnett@protonmail.com','L-~I6pOy42MYY#y','private mail');
            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (142,'Web','office365.com','ninaviola1','OfficeSpace##1','company email');
            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (142,'Web','facebook.com','ninaviola91','19911991#10','throwaway fb');
            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (143,'App','Netflix','alvinfisher1979','efQKL2pJAWDM46L7','Family Netflix');
            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (143,'Web','twitter.com','alvinfisher1979','7wYz9pbbaH3S64LG','old twitter account');
            INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (143,'Email','outlook.com','alvinfisher1979@outlook.com','jJGYu4j8tYakBY9u','work mail');
        `);
    }

    async getLastUuid() {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('SELECT uuid from users ORDER BY rowid DESC LIMIT 1;');
                resolve(await stmt.get());
            } catch(e) {
                reject(e);
            }
        });
    }

    async registerUser(user, pass, email, uuid) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('INSERT INTO users (username, password, email, uuid) VALUES ( ?, ?, ?, ?)');
                resolve((await stmt.run(user, pass, email, uuid)));
            } catch(e) {
                console.log(e);
                reject(e);
            }
        });
    }

    async loginUser(user, pass) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('SELECT username FROM users WHERE username = ? and password = ?');
                resolve(await stmt.get(user, pass));
            } catch(e) {
                reject(e);
            }
        });
    }

    async getUser(user) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('SELECT * FROM users WHERE username = ?');
                resolve(await stmt.get(user));
            } catch(e) {
                reject(e);
            }
        });
    }

    async checkUser(user) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('SELECT username FROM users WHERE username = ?');
                let row = await stmt.get(user);
                resolve(row !== undefined);
            } catch(e) {
                reject(e);
            }
        });
    }

    
    async getSavedPasswords(uuid) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('SELECT * FROM user_data WHERE uuid = ?');
                resolve(await stmt.all(uuid));
            } catch(e) {
                reject(e);
            }
        });
    }

    async addPassword(uuid, recType, recAddr, recUser, recPass, recNote) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('INSERT INTO user_data (uuid,type,address,username,password,note) VALUES (?, ?, ?, ?, ?, ?)');
                resolve((await stmt.run(uuid, recType, recAddr, recUser, recPass, recNote)));
            } catch(e) {
                reject(e);
            }
        });
    }

    async delPassword(uuid, passId) {
        return new Promise(async (resolve, reject) => {
            try {
                let stmt = await this.db.prepare('DELETE FROM user_data WHERE uuid = ? and id = ?');
                resolve(await stmt.all(uuid,passId));
            } catch(e) {
                reject(e);
            }
        });
    }

}

module.exports = Database;