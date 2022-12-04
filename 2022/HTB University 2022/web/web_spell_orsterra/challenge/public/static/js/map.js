$(document).ready(() => {
    loadtrackers();
	var fadeBackground = $(document.createElement("div"))
			.hide()
			.attr("id", "fade-background"),
		modalWindow = $(document.createElement("div"))
			.hide()
			.attr("id", "modal-location");
	$(document.body).append(fadeBackground, modalWindow);
	$(document).on("click", ".modal-link", function (e) {
        var content = $("#" + $(this).data("modal-target")).html();
        var uuid = $(this).data("uuid");
        var coor_y = $(this).data("y-coordinate");
        var coor_x = $(this).data("x-coordinate");
        var spell  = $(this).data('live-spell');

		$("#fade-background").css({ opacity: "0.85" }).fadeIn("fast");

		$("#modal-location").html(content);
        $('.coor_y').text(coor_y);
        $('.coor_x').text(coor_x);
        $('.uuid_info').text(uuid);

		$("#modal-location").fadeIn("fast");

        $('.spell-cast-btn').on('click', () => { applySpell(uuid, coor_y, coor_x)});
        if (spell) {
            $('.spell-cast-btn').prop('disabled', true);
            $('.spell-cast-btn').html('Spell already casted &nbsp;<i class="fas fa-flask-potion"></i>');
            $('.spell-email-inp').hide();
        }
        else {
            $('.spell-cast-btn').prop('disabled', false);
            $('.spell-cast-btn').html('Cast Tracker Spell &nbsp;<i class="fas fa-flask-potion"></i>');
            $('.spell-email-inp').show();
        }

        e.preventDefault();
	});
	$(document).on("click", "#fade-background", function () {
		$("#fade-background").fadeOut("fast");
		$("#modal-location").fadeOut("fast");
	});

});

const loadtrackers = async () => {
    await fetch(`/api/tracker/list`, {
        method: 'GET',
        credentials: 'include'
    })
    .then((response) => response.json()
        .then((data) => {
            for (let track of data) {
                populateMap(track);
            }
        }))
    .catch((error) => {
        console.error(error);
    });
}

const populateMap = (track) => {
    $('#track-count').text(parseInt($('#track-count').text()) + 1);

    let spellHTML = ''
    if (track['live-spell'] == 1) {
        spellHTML = `<img src="/static/images/spell.gif" class="${track.uuid}-spell spell track-spell" id="${track.uuid}-spell"></img>`;

        $('#spell-count').text(parseInt($('#spell-count').text()) + 1);
    }

    let trackHTML = `
    <a href="#" class="modal-link"
        data-modal-target="main-data-modal"
        data-uuid="${track.uuid}"
        data-x-coordinate="${track['x-coordinate']}"
        data-y-coordinate="${track['y-coordinate']}"
        data-live-spell="${track['live-spell']}"
    >
        <div class="track ${track.uuid}"></div>
        ${spellHTML}
    </a>`;

    $('.orsterra-points').first().append(trackHTML);
    $(`.${track.uuid}`).css('top', track['y-coordinate']);
    $(`.${track.uuid}`).css('left', track['x-coordinate']);
    $(`.${track.uuid}-spell`).css('top', track['y-coordinate']);
    $(`.${track.uuid}-spell`).css('left', track['x-coordinate']);

}

const applySpell = async (uuid, coor_y, coor_x) => {
    let email = $(".spell-email-inp")[1].value;
    
	if ($.trim(email) === '') {
		showToast("Please input an email first!");
        $("#fade-background").fadeOut("fast");
        $("#modal-location").fadeOut("fast");
		return;
	}

	await fetch(`/api/tracker/subscribe`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
                email,
                uuid
            }),
		})
		.then(async (response) => {
            if (response.status !== 200) {
                data = await response.json();
				showToast(data.message);
            }
            else {
                location.reload();
            }
		})
		.catch((error) => {
			showToast(error.message);
		});

    $("#fade-background").fadeOut("fast");
    $("#modal-location").fadeOut("fast");
}

const showToast = (msg, fixed=false) => {
    $('#globalToast').hide();
    $('#globalToast').slideDown();
    $('#globalToastMsg').text(msg);
    if (!fixed) {
        setTimeout(() => {
            $('#globalToast').slideUp();
        }, 2500);
    }
}

$(".locfaction.cagliostro").click(function () {
	$(".area.cagliostro").toggleClass("area-active");
});

$(".locfaction.farnessa").click(function () {
	$(".area.farnessa").toggleClass("area-active");
});

$(".locfaction.atmahata").click(function () {
	$(".area.atmahata").toggleClass("area-active");
});

$(".locfaction.tarpuz").click(function () {
	$(".area.tarpuz").toggleClass("area-active");
});

$(".tog-city").click(function () {
	$(".location").toggleClass("toggle-hide");
});
$(".tog-dung").click(function () {
	$(".track").toggleClass("toggle-hide");
});
$(".tog-feat").click(function () {
	$(".orsterra-features").toggleClass("toggle-hide");
});

