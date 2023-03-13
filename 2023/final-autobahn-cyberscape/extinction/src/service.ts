import { Payload, ListQuery, Code } from "./type.ts";
import { CodeRepository } from "./database.ts";

export class Service {
    private readonly repository: CodeRepository;

    constructor() {
        this.repository = new CodeRepository();
    }

    create(user: Payload, data: any) {
        this.repository.create({ user, ...data})
    }

    list(user: Payload, data?: any) {
        const defaultQuery: Partial<ListQuery> = { fuzzy: '', limit: -1, offset: -1 };
        const query = { ...defaultQuery, ...data}
    
        const codes = this.repository.list({ user, ...query });
        const result: Partial<Code>[] = [];

        codes.forEach((code: any) => {
            const [slug] = code;
            result.push(slug);
        });

        return result;  
    }

    get(slug: string) {
        return this.repository.get(slug);
    }
}

