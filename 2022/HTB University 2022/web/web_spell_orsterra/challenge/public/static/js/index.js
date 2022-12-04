window.onload = async () => {
    $('#subscribeBtn').on('click', subscribe);

    statusConfig = await fetchServices();
    populateStatus(statusConfig);
}

const fetchServices = async () => {
    services = await fetch('/api/service/list')
    .then((response) => response.json()
        .then((data) => {
            return data;
        }))
    .catch((error) => {
        showToast(error.message);
    });
    return services;
};

const subscribe = async () => {

	let email = $("#email").val();
	if ($.trim(email) === '') {
		showToast("Please input an email first!");
		return;
	}

	await fetch(`/subscribe`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({email}),
		})
		.then((response) => response.json()
			.then((resp) => {
				showToast(resp.message);
			}))
		.catch((error) => {
			showToast(error.message);
		});

}

const populateStatus = async (statusConfig) => {
    let longCards;
    let statCards;
    statusConfig.forEach(service => {
        if (service.status == 3) {
            longCards += `
                <div class="alert alert-danger d-flex align-items-center justify-content-between" role="alert">
                    <div class="flex-fill mr-3">
                    <p class="mb-0">${service.service} is experiencing issues.</p>
                    </div>
                    <div class="flex-00-auto">
                    <i class="fa fa-fw fa-2x fa-bug"></i>
                    </div>
                </div>`;
            statCards += `
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    ${service.service}
                    <span class="badge badge-pill badge-danger">Down</span>
                </li>`;
        }
        else if(service.status == 2) {
            longCards += `
                <div class="alert alert-warning d-flex align-items-center justify-content-between" role="alert">
                    <div class="flex-fill mr-3">
                    <p class="mb-0">${service.service} is currently under maintenance. </p>
                    </div>
                    <div class="flex-00-auto">
                    <i class="fa fa-fw fa-2x fa-exclamation-triangle"></i>
                    </div>
                </div>`;
            statCards += `
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    ${service.service}
                    <span class="badge badge-pill badge-warning">Maintenance</span>
                </li>`;
        }
        else {
            statCards += `
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    ${service.service}
                    <span class="badge badge-pill badge-success">Operational</span>
                </li>`;
        }
    });

    $('.stats-longcards').html(longCards);
    $('.stats-statcards').html(statCards);

};


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