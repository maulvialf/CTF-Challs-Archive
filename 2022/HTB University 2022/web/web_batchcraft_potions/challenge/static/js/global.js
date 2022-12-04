window.potionTypes = [
    {
        "id": 1,
        "name":"Snake Charm",
        "src":"/static/images/snakecharm.jpg"
    },
    {
        "id": 2,
        "name":"Fairy Dust",
        "src":"/static/images/fairydust.jpg"
    },
    {
        "id": 3,
        "name":"Gemini Stone",
        "src":"/static/images/geministone.jpg"
    },
    {
        "id": 4,
        "name":"Fire Born",
        "src":"/static/images/fireborn.jpg"
    },
    {
        "id": 5,
        "name":"Dragon Breath",
        "src":"/static/images/dragonbreath.jpg"
    },
    {
        "id": 6,
        "name":"Dark Spell",
        "src":"/static/images/darkspell.jpg"
    }
]

const showToast = (msg, fixed=false) => {
    $('#globalToast').hide();
    $('#globalToast').show();
    $('#globalToastMsg').text(msg);
    if (!fixed) {
        setTimeout(() => {
            $('#globalToast').hide();
        }, 2500);
    }
}