export type Payload = {
    username: string;
    role: string;
};

export type Code = {
    user: Payload;
    slug: string;
    data: string;
    is_private: boolean;
}

export type ListQuery = {
    user: Payload;
    fuzzy: string;
    limit: number;
    offset: number;
}