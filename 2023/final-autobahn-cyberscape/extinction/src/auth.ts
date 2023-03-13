import { create, decode, Header } from 'https://deno.land/x/djwt@v2.2/mod.ts'
import { Payload } from './type.ts';

export class Auth {
    public readonly secret: string;
    public readonly header: Header;
    public readonly cookie: string;


    constructor() {
        this.secret = Deno.env.get('SECRET') || 'CHANGEME';
        this.header = { alg: 'HS512', typ: 'JWT' };
        this.cookie = 'access_token';
    }

    async generateToken(payload: Payload) {
        return await create(this.header, {...payload, role: 'user'}, this.secret);
    }

    decodeToken(token: string){
        const [_, payload, ] = decode(token);
        return payload as Payload;
    }
}
