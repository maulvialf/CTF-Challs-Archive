import { wrapFetch } from "https://deno.land/x/another_cookiejar@v5.0.3/mod.ts"

import { extractOrigin, extractObject } from "./util.ts"

export class CTFd {
    url: string
    name: string
    password: string
    fetch: typeof fetch

    constructor(url: string, name: string, password: string) {
        this.name = name
        this.password = password
        this.url = extractOrigin(url)
        this.fetch = wrapFetch()
    }   

    async getNonce() {
        const response = await this.fetch(`${this.url}/login`, { method: 'GET'})
        const text = await response.text()
        const nonce = text.match(/csrfNonce': "(.*)"/)?.pop() ?? '' 

        return nonce
    }

    async login(nonce: string) {
        const body = new URLSearchParams({
            name: this.name,
            password: this.password,
            nonce: nonce,
        })

        const response = await this.fetch(`${this.url}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: body.toString(),
        })

        const text = await response.text()
        return !text.includes('incorrect')
    }

    async getChallenges() {
        const response = await this.fetch(`${this.url}/api/v1/challenges`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })

        return extractObject(response.json())
    }

    async getChallengeDetail(id: string) {
        const response = await this.fetch(`${this.url}/api/v1/challenges/${id}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })

        return extractObject(response.json())
    }
}