import { sha256 } from "https://denopkg.com/chiefbiiko/sha256@v1.0.0/mod.ts"

export const extractOrigin = (str: string) => {
    const url = new URL(str)
    return url.origin
}

export const extractObject = async (data: object) => {
    return Object.values(await data).reduce((result, element) => {
        if (!result && typeof element === 'object') { return element }
        return result
    }, null)
}

export const hashObject = (obj: object) => {
    return sha256(JSON.stringify(obj), 'utf8', 'hex')
}

export const sleep = (ms: number) => {
    return new Promise(resolve => setTimeout(resolve, ms))
}
