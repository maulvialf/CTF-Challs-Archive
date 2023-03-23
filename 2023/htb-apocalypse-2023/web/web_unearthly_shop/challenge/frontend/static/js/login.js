const form     = document.getElementById('form');
const alerts   = document.getElementById('alerts');

const flash = data => {
	let { message, status } = data;

	alerts.className = `alert alert-${status} mt-3`;
    alerts.innerText = message;
	alerts.style.display = 'block';

	setTimeout(() => {
		alerts.style.display = 'none';
	}, 3000);
};

form.addEventListener('submit', async e => {
	e.preventDefault();
	intent = e.submitter.id.match(/[^-]*/)[0];

	if (intent == 'register') data['email'] = email;

	const response = await fetch(`/admin/api/auth/${ intent }`, {
		method: 'POST',
		body: new URLSearchParams(new FormData(e.target))
	});

	const isJson = response.headers.get('content-type')?.includes('application/json');
	const data = isJson ? await response.json() : null;

	const error = {
		message: 'Something went wrong',
		status:  'danger',
	};

	if (data) {
		if (response.ok) {
			if (intent == 'login') {
				flash(data)
				window.location.href = '/admin/dashboard';
				return;
			}

			flash(data)
			window.location.href = '/admin/';
			return;
		}

		flash(data);
        return;
	}
    flash(error);
});