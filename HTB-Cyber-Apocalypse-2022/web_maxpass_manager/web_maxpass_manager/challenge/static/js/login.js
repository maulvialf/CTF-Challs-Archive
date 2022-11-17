$(document).ready(function() {

	// set input event
	$("#login-btn").on('click', login);
});

function toggleInputs(state) {
	$("#username").prop("disabled", state);
	$("#password").prop("disabled", state);
	$("#login-btn").prop("disabled", state);
}


async function login() {

	toggleInputs(true); // disable inputs

	// prepare alert
	let card = $("#resp-msg");
	card.hide();


	let user = $("#username").val();
	let pass = $("#password").val();

	// validate
	if ($.trim(user) === '' || $.trim(pass) === '') {
		toggleInputs(false);
		card.text("Please fill out all the required fields!");
		card.attr("class", "alert alert-danger");
		card.show();
		return;
	}

	const data = {
		username: user,
		password: pass
	};

	await fetch("/api/login", {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					card.text(resp.message);
					card.attr("class", "alert alert-success");
					card.show();
					window.setTimeout(function() {
						window.location.href = '/dashboard';
					}, 600);
					return;
				}
				card.text(resp.message);
				card.attr("class", "alert alert-danger");
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.attr("class", "alert alert-danger");
			card.show();
		});

	toggleInputs(false); // enable inputs
}