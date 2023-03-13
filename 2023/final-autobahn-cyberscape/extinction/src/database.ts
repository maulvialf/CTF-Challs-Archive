import { DB } from 'https://deno.land/x/sqlite@v3.7.0/mod.ts';
import { Code, ListQuery } from './type.ts';

export const db = new DB('extinction.db');


export class CodeRepository {
    private db: DB;

    constructor() {
        this.db = db
    }
    
    create(code: Code) {
        this.db.query(
            'INSERT INTO codes (slug, data, author, is_private) VALUES (?, ?, ?, ?)', 
            [code.slug, code.data, code.user.username, code.is_private]
        );
    }

    list(query: ListQuery) {
        const is_admin = query.user.role === 'admin';
        const codes = this.db.query(
            'SELECT slug FROM codes WHERE (? OR author = ? OR is_private = 0) AND data LIKE ? LIMIT ? OFFSET ?',
            [is_admin, query.user.username, `%${query.fuzzy}%`, query.limit, query.offset]
        );
        
        return codes;
    }

    get(slug: string) {
        const [code] = this.db.query('SELECT data FROM codes WHERE slug = ?', [slug]);
        return code as unknown as string;
    }
}
