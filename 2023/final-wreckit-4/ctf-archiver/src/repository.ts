import { msClient } from "./init.ts"
import { Challenge, Payload } from "./type.ts"
import { hashObject } from './util.ts'

export class Repository {

    client = msClient

    async insertArchive(archive: Payload) {
        const index = this.client.index('archives')
        const { password, ...payload } = archive
        const is_public = !!payload.is_public

        const id = hashObject(archive)
        const documents = [{ id, ...payload, is_public}]

        await index.addDocuments(documents)
        return id as string
    }

    async getArchive(id: string) {
        const index = this.client.index('archives')
        try {
            const document = await index.getDocument(id)
            return document
        } catch (error) {
            console.log(error)
            return null
        }
    }

    getPublicArchives(query: string) {
        const index = this.client.index('archives')
        return index.search(query, { filter: ['is_public=true'] })
    }

    insertChallenges(id: string, challenges: Challenge[]) {
        const index = this.client.index('challenges')
        return index.addDocuments([{ id, challenges }])
    }

    async getChallenges(id: string) {
        const index = this.client.index('challenges')
        try {
            const document = await index.getDocument(id)
            return document
        } catch (error) {
            console.log(error)
            return null
        }
    }
}