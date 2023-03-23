window.onload = () => {
    get_orders();
}

const htmlEncode = (str) => {
	return String(str).replace(/[^\w. ]/gi, function(c) {
		return '&#' + c.charCodeAt(0) + ';';
	});
}

const get_orders = () => {
    ordersTable = $('#orders-table');
    ordersTable.find('tbody').html('');
    fetch('/admin/api/orders/list')
    .then(resp => resp.json())
    .then(data => {
        if(data.hasOwnProperty('orders')) {
            ordersTable.show();
            for(let order of data.orders) {
                if (typeof order._id === "object") order._id = order._id['$oid'];
                let template = `
                <tr>
                    <td class="numbers">${ htmlEncode(order._id) }</td>
                    <td>${ htmlEncode(order.name) }</td>
                    <td class="numbers">${ htmlEncode(order.email) }</td>
                    <td class="numbers">${ htmlEncode(order.item_id) }</td>
                    <td><span class="numbers">${ htmlEncode(order.bid) }</span> mill</td>
                    <td>
                        <button class="btn btn-secondary p-1 ps-3 pe-3" onclick="editOrder(${order._id})">Edit</button>&nbsp;
                        <button class="btn btn-danger p-1 ps-3 pe-3" onclick="editOrder(${order._id})">Delete</button>
                    </td>
                </tr>`;
                ordersTable.find('tbody').append(template);
            }
        }

    });
};
