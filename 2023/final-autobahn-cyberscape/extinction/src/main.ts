import { serve } from "https://deno.land/std@0.179.0/http/server.ts"
import { Hono } from 'npm:hono'
import { jwt } from 'npm:hono/jwt'
import { Service } from "./service.ts"
import { Auth } from './auth.ts'
import { database } from "./init.ts"

database()

const app = new Hono()
const service = new Service()
const auth = new Auth()
const { secret, header: { alg }, cookie} = auth

const getUser = (c: any) => {
    const token = c.req.cookie(auth.cookie) || ''
    if (!token) return c.redirect('/')
    return auth.decodeToken(token)
}

app.use('/codes/*', jwt({ secret, alg, cookie}))

app.get('/codes', (c) => {
    const user = getUser(c)
    const codes = service.list(user)
    return c.json(codes)
})

app.post('/codes', async (c) => {
    const user = getUser(c)
    const data = await c.req.json()
    const code = service.list(user, data)
    return c.json(code)
})

app.post('/codes/', async (c) => {
    const user = getUser(c)
    const data = await c.req.json()
    const code = service.create(user, data)
    return c.json(code)
})

app.get('/codes/:slug', (c) => {
    const slug = c.req.param('slug')
    const code = service.get(slug)
    return c.text(code)
})

app.post('/register', async (c) => {
    const data = await c.req.json()
    const token = await auth.generateToken(data)
    c.cookie(cookie, token)
    return c.text(token)
})

app.get('/', (c) => {
    return c.json({ service: 'extinction' })
})

serve(app.fetch)
