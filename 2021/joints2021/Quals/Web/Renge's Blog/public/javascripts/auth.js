async function auth()
{
    await fetch("/auth",{
        method: 'GET',
        credentials: 'same-origin'
    })
}

auth()