$(document).ready(function() {
	$('#verify-btn').on('click', login);
});

const toggleInputs = (state) => {
	$('#username').prop('disabled', state);
	$('#password').prop('disabled', state);
	$('#verify-btn').prop('disabled', state);
}


const login = async () => {

	toggleInputs(true);

	let card = $('#resp-msg');
	card.hide();

	let otp = $('#otp').val();

	if ($.trim(otp) === '') {
		toggleInputs(false);
		card.text('Please submit a valid OTP token!');
		card.attr('class', 'alert alert-danger');
		card.show();
		return;
	}

	await fetch('/graphql', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
                query: 'mutation($otp: String!) { verify2FA(otp: $otp) { message, token } }',
                variables: {
                    'otp': otp
                }
            }),
		})
		.then((response) => response.json())
        .then((response) => {
            if (response.data.verify2FA) {
                card.text(response.data.verify2FA.message);
                card.attr('class', 'alert alert-success');
                card.show();
                window.setTimeout(function() {
                    window.location.href = '/dashboard';
                }, 600);
                return;
            }
            else if (response.hasOwnProperty('errors')) {
                card.text(response.errors[0].message);
            }
            else {
                card.text('Something went wrong!');
            }
            card.attr('class', 'alert alert-danger');
            card.show();
        })
		.catch((error) => {
			card.text(error);
			card.attr('class', 'alert alert-danger');
			card.show();
		});

	toggleInputs(false);
}
