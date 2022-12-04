

$(document).ready(() => {
	$('#showAddForm').on('click', showForm);
	$('#cancel-btn').on('click', hideForm);
	$('#add-btn').on('click', addProduct);
});

const showForm = () => {
	$('#products-view').hide();
	$('#add-product-view').slideDown("slow");
}

const hideForm = () => {
	$('#products-view').slideDown();
	$('#add-product-view').hide();
}

const addProduct = async () => {
	const card = $('#add-resp-msg');

	card.attr("class", "alert alert-info");
	card.text('Please wait...');
	card.show();

	$form = $('#addForm');
	const formData = getFormData($form);

	await fetch('/api/products/add', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(formData)
		})
		.then(response => response.json()
			.then(resp => {
				card.attr("class", "alert alert-danger");
				if (response.status == 200) {
					card.attr("class", "alert alert-success");
					setTimeout(() => {
						location.reload()
					}, 1000);
				}
				if (resp.hasOwnProperty('message')) {
					card.text(resp.message);
					card.show();
				}
			}))
		.catch((error) => {
			console.log(error);
		});
}

const getFormData = ($form) => {
	var unindexed_array = $form.serializeArray();
	var indexed_array = {};
	$.map(unindexed_array, (n, i) => {
		indexed_array[n['name']] = n['value'];
	});
	return indexed_array;
}