import { serve } from "https://deno.land/std@0.179.0/http/server.ts"
import { Hono } from 'npm:hono'

import { Service } from "./service.ts"
import { initMeiliSearch } from "./init.ts"
import { Payload } from "./type.ts"

const app = new Hono()
const service = new Service()

initMeiliSearch()

app.get('/', async (c) => {
    const query = c.req.query('search') ?? ''
    return c.html(await service.index(query))
})

app.get('/archive', async (c) => {
    return c.html(await service.archiveIndex())
})

app.post('/archive', async (c) => {
    const body = await c.req.parseBody()
    const id = await service.archive(body as Payload)
    return c.redirect(`/download?id=${id}`)
})

app.get('/download', async (c) => {
    const id = c.req.query('id')

    if (!id) {
        return c.notFound()
    }

    const archive = await service.download(id as string)

    if (!archive) {
        return c.notFound()
    }

    c.res.headers.set('Content-Disposition', `attachment; filename=${id}.json`)
    return c.json(archive)
})

serve(app.fetch)
