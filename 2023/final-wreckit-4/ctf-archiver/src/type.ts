export type Payload = {
    url: string
    name: string
    username: string
    password: string
    is_public?: string
}

export type Challenge = {
    name: string
    value: number
    description: string
    category: string
    attachments: string[]
}