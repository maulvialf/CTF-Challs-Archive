import { MeiliSearch } from 'npm:meilisearch'

export const msClient = new MeiliSearch({ host: 'http://meilisearch:7700' })

export const initMeiliSearch = () => {
    msClient.createIndex('archives', { primaryKey: 'id' })
    const archives = msClient.index('archives')
    archives.updateFilterableAttributes(['is_public'])

    msClient.createIndex('challenges', { primaryKey: 'id' })
}

