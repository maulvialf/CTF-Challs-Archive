<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="style.css">
    <title>Waifu Terbaik</title>
</head>
<body>
    <div class="w3-container w3-center">
        <div class="w3-card-4">
            <header class="w3-container w3-black">
                <h1>Voting Waifu Terbaik</h1>
            </header>

            <div class="w3-container">
                <div class="w3-row">
                    <div class="w3-quarter">
                        <div class="w3-card-4 w3-purple chara-card">
                            <div class="w3-container w3-center">
                                <h3><b>Keqing</b></h3>
                                <img src="https://rerollcdn.com/GENSHIN/Characters/Keqing.png" alt="Avatar" style="width:80%">
                                <h5 id="vote-count-keqing">0 Vote</h5>
                                <button class="w3-button w3-green vote-button" onclick="vote('keqing')">Vote</button>
                            </div>
                        </div>
                    </div>

                    <div class="w3-quarter">
                        <div class="w3-card-4 w3-pale-green chara-card">
                            <div class="w3-container w3-center">
                                <h3><b>Jean</b></h3>
                                <img src="https://rerollcdn.com/GENSHIN/Characters/Jean.png" alt="Avatar" style="width:80%">
                                <h5 id="vote-count-jean">0 Vote</h5>
                                <button class="w3-button w3-green vote-button" onclick="vote('jean')">Vote</button>
                            </div>
                        </div>
                    </div>

                    <div class="w3-quarter">
                        <div class="w3-card-4 w3-pink chara-card">
                            <div class="w3-container w3-center">
                                <h3><b>Hu Tao</b></h3>
                                <img src="https://rerollcdn.com/GENSHIN/Characters/Hu%20Tao.png" alt="Avatar" style="width:80%">
                                <h5 id="vote-count-hutao">0 Vote</h5>
                                <button class="w3-button w3-green vote-button" onclick="vote('hutao')">Vote</button>
                            </div>
                        </div>
                    </div>

                    <div class="w3-quarter">
                        <div class="w3-card-4 w3-blue chara-card">
                            <div class="w3-container w3-center">
                                <h3><b>Ganyu</b></h3>
                                <img src="https://rerollcdn.com/GENSHIN/Characters/Ganyu.png" alt="Avatar" style="width:80%">
                                <h5 id="vote-count-ganyu">0 Vote</h5>
                                <button class="w3-button w3-green vote-button" onclick="vote('ganyu')">Vote</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <footer class="w3-container w3-black">
                <h5>JOINTS 2021 CTF</h5>
            </footer>
        </div>
    </div>

    <script>
        const waifu = [
            'keqing', 'jean', 'hutao', 'ganyu'
        ]

        function fetchWaifuVotesCount (waifu) {
            fetch(`/api.php?character=${waifu}`)
                .then(response => response.json())
                .then(results => {
                    const vote_count_html = document.querySelector(`#vote-count-${waifu}`)
                    const total_vote = results.data.vote_count

                    if (total_vote > 1) {
                        vote_count_html.innerHTML = `${total_vote} Votes`
                    } else {
                        vote_count_html.innerHTML = `${total_vote} Vote`
                    }
                })
        }

        function vote (waifu) {
            const formData = new FormData()
            formData.append('character', waifu)

            fetch('/api.php', {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(result => {
                    if (result.success) {
                        fetchWaifuVotesCount(waifu)
                        alert('sukses melakukan voting')
                    } else {
                        alert(result.error)
                    }
                })
                .catch(error => {
                    alert('error');
                });

        }

        waifu.forEach(item => {
            fetchWaifuVotesCount(item)
        })
    </script>

    <!-- credit: cacadosman -->
</body>
</html>