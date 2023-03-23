window.onload = () => {
    $('#back-user-btn').on('click', () => {
        $('#users-container').show();
        $('#user-view-container').hide();
    });

    get_users();
}

const htmlEncode = (str) => {
	return String(str).replace(/[^\w. ]/gi, function(c) {
		return '&#' + c.charCodeAt(0) + ';';
	});
}

const get_users = () => {
    usersTable = $('#users-table');
    usersTable.find('tbody').html('');
    fetch('/admin/api/users/list')
    .then(resp => resp.json())
    .then(data => {
        if(data.hasOwnProperty('users')) {
            usersTable.show();
            for(let user of data.users) {
                let template = `
                <tr>
                    <td class="numbers">${ htmlEncode(user._id) }</td>
                    <td>${ htmlEncode(user.username) }</td>
                    <td><button class="btn btn-secondary p-1 ps-3 pe-3" onclick="editUser(${user._id})">Edit</button></td>
                </tr>`;
                usersTable.find('tbody').append(template);
            }
        }

    });
};

const editUser = (id) => {
    $('#users-container').hide();
    $('#user-view-container').show();

    $('#user-card').html('');
    fetch(`/admin/api/users/${id}`)
    .then(resp => resp.json())
    .then(data => {
        if(data.hasOwnProperty('user')) {
            populateuserView(data.user);
        }

    });
}


const populateuserView = (user) => {
    userCard = $('#user-card');
    let template = `
        <h5 class="card-header text-uppercase">user <span class="numbers">#${ htmlEncode(user._id) }</span></h5>
        <div class="card-body">
            <div class="row">
                <div class="col-md-2">
                    <p class="fw-bold user-label pt-2">username: </p>
                </div>
                <div class="col-md">
                    <input type="text" class="form-control" id="username" value="${ htmlEncode(user.username) }">
                </div>
            </div>
            <div class="row">
                <div class="col-md-2">
                    <p class="fw-bold user-label pt-2">password: </p>
                </div>
                <div class="col-md">
                    <input type="text" class="form-control" id="password" value="">
                </div>
            </div>
            <div class="row">
                <div class="col text-center">
                    <button class="btn btn-secondary m-auto" onclick="updateUser(${user._id})">Update User</button>
                </div>
            </div>
            <p class="alert alert-info" id="resp-msg">Please wait</p>

        </div>
        `;
    userCard.append(template);
}

const updateUser = (_id) => {
    card = $('#resp-msg');
    card.text('Please wait');
    card.show();

    username = $('#username').val();
    password = $('#password').val();

    if ($.trim(password) == '' || $.trim(username) == '') {
        card.text('Please input the required fields first');
        return;
    }

    fetch('/admin/api/users/update', {
		method: 'POST',
		body: JSON.stringify({_id, username, password})
	})
    .then(resp => resp.json())
    .then(data => {
        card.text(data.message);
    })
    .catch(e => {
        card.text('Something went wrong');
        console.log(e);
    });
}
