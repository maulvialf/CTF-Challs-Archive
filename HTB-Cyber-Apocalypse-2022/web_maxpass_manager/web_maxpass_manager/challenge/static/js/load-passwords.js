$(document).ready(function() {
	loadPasswords();
});

async function loadPasswords() {

	await fetch(`/api/passwords/${user_uuid}`, {
			method: 'GET',
			credentials: 'include'
		})
		.then((response) => response.json())
		.then((userData) => populateTable(userData))
		.catch((error) => console.log(error));
}

function populateTable(userData) {

	$('#password-listing tbody').empty();
	$("#empty-table-msg").show();
	$("#password-listing").hide();

	if (userData.passwords.length !== 0) {
		let passList = userData.passwords;

		for (entry in passList) {
			passInfo = passList[entry];

			rowData = `<tr id="${passInfo.id}_row">`;

			if (passInfo.type == "Email") {
				rowData += "<td>✉️ mail</td>";
			} else if (passInfo.type == "App") {
				rowData += "<td>📱 app</td>";
			} else {
				rowData += "<td>🌐 web</td>";
			}


			rowData += `<td>${passInfo.address}</td>`;
			rowData += `<td>${passInfo.username}</td>`;
			rowData += `<td><span class="hidden" id="${passInfo.id}_visible">${passInfo.password}</span><span id="${passInfo.id}_hidden">********</span></td>`;
			rowData += `<td>${passInfo.note}</td>`;
			rowData += `<td>
                              <button type="button" class="btn btn-sm btn-dark btn-icon-text" onclick="togglePassView('${passInfo.id}')" id="${passInfo.id}_vBtn">
                                  <i class="mdi mdi-eye btn-icon"></i>
                              </button>
                              <button type="button" class="btn btn-sm btn-dark btn-icon-text" onclick="delPassData('${passInfo.id}')">
                                  <i class="mdi mdi-delete btn-icon"></i>                          
                              </button>
                        </td>
                </tr>`;

			$('#password-listing > tbody:last-child').append(rowData);
		}

		$("#empty-table-msg").hide();
		$("#password-listing").show();
	}

}