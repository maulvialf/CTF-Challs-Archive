import { db } from "./database.ts";

export const database = () => {
    db.execute(`CREATE TABLE IF NOT EXISTS codes ( slug TEXT UNIQUE, data TEXT, author TEXT, is_private INTEGER )`);
}

export const secret = () => {
    const rand = crypto.randomUUID().toString();
    Deno.env.set("SECRET", rand);
    return rand;
};