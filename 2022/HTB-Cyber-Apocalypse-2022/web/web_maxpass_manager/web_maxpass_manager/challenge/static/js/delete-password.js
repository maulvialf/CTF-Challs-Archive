async function delPassData(pRowId) {

	const data = {
		passId: pRowId
	};

	await fetch("/api/passwords/delete", {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					loadPasswords();
					return;
				}
			}))
		.catch((error) => {
			console.log(error);
		});

	toggleInputs(false); // enable inputs
}