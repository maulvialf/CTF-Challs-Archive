$(document).ready(function() {
	fetch_firmwares();
	$('#cancel-btn').on('click', hide_report);
	$('#report-btn').on('click', report);
});


const fetch_firmwares = async () => {

	await fetch(`/api/firmware/list`, {
		method: 'GET',
		credentials: 'include',
	})
	.then((response) => response.json()
		.then((resp) => {
			for (firmware of resp) {
				rowData = `<tr>
					<th scope="row">${firmware.id}</th>
					<td>${firmware.module}</td>
					<td>${firmware.hw_version}</td>
					<td>${firmware.fw_version}</td>
					<td>${firmware.serial}</td>
					<td>${firmware.hub_id}</td>
					<td><button class="btn btn-primary report-btn" onclick="report_box(${firmware.id}, '${firmware.module}')">Report a bug</button></td>
				</tr>`;
				$('#firmware-table > tbody').append(rowData);

			}
		}))
	.catch((error) => {
		console.error(error)
	});
}

const report_box = (id, name) => {
	$('#module-name').text(name);
	$('#module-id').val(id);
	$('.firmware-area').hide();
	$('.report-area').slideDown();
}

const hide_report = () => {
	$('.report-area').hide();
	$('.firmware-area').slideDown();
}

const report = async() => {
	$('#report-btn').prop('disabled', true);

	// prepare alert
	let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.text("Submitting your report, please wait...");
	card.show();

	// validate
	let issue = $("#issue").val();
	let module_id = $("#module-id").val();
	if ($.trim(issue) === '') {
		$('#report-btn').prop('disabled', false);
		card.text("Please input your issue first!");
		card.attr("class", "alert alert-danger");
		card.show();
		return;
	}

	await fetch(`/api/firmware/report`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ module_id, issue }),
		})
		.then((response) => response.json()
			.then((resp) => {
				card.attr("class", "alert alert-danger");
				if (response.status == 200) {
					card.attr("class", "alert alert-info");
					card.text(resp.message);
					card.show();
					return;
				}
				card.text(resp.message);
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.attr("class", "alert alert-danger");
			card.show();
		});

		$('#report-btn').prop('disabled', false);
}