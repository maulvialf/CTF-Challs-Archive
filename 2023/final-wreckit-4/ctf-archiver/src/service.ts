import { renderFile, configure } from "https://deno.land/x/eta@v1.11.0/mod.ts"

import { CTFd } from "./ctfd.ts"
import { Repository } from "./repository.ts"
import { Payload } from "./type.ts"
import { sleep } from "./util.ts"

const viewPath = `${Deno.cwd()}/views/`

configure({ views: viewPath })


export class Service {
    private readonly repository: Repository

    constructor() {
        this.repository = new Repository()
    }

    async index(query: string) {
        const { hits } = await this.repository.getPublicArchives(query)
        return renderFile("./index", { ctfs: hits })
    }

    archiveIndex() {
        return renderFile("./archive", {})
    }

    async archive(payload: Payload) {
        const { url, username, password, is_public } = payload

        const ctfd = new CTFd(url, username, password)
        const nonce = await ctfd.getNonce()
        
        if (!nonce) {
            return { status: 401, message: 'Invalid URL'}
        }

        if (!await ctfd.login(nonce)) {
            return { status: 401, message: 'Login failed'}
        }

        const challenges = await ctfd.getChallenges()
        const id = await this.repository.insertArchive(payload)

        const transformed = []

        for (const challenge of challenges) {
            const attachments = []
            const detail = await ctfd.getChallengeDetail(challenge.id)
            
            for (const file of detail.files) {
                const attachment = `${url}${file}`
                attachments.push(attachment)
            }

            transformed.push({
                name: challenge.name,
                value: challenge.value,
                category: challenge.category,
                description: detail.description,
                connection_info: detail.connection_info,
                attachments
            })
        }

        await this.repository.insertChallenges(id, transformed)
        return id
    }

    async download(id: string) {
        const archive = await this.repository.getArchive(id)
        if (!archive) { return null }

        let challenges
        
        while (!challenges) {
            await sleep(1000)
            challenges = await this.repository.getChallenges(id)
        }

        return {
            ...archive,
            challenges
        }
    }

}

