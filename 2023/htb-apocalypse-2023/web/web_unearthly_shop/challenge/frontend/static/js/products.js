window.onload = () => {
    get_products();
}

const htmlEncode = (str) => {
	return String(str).replace(/[^\w. ]/gi, function(c) {
		return '&#' + c.charCodeAt(0) + ';';
	});
}

const get_products = () => {
    productsTable = $('#products-table');
    productsTable.find('tbody').html('');
    fetch('/admin/api/products/list')
    .then(resp => resp.json())
    .then(data => {
        if(data.hasOwnProperty('products')) {
            productsTable.show();
            for(let product of data.products) {
                let template = `
                <tr>
                    <td class="numbers">${ htmlEncode(product._id) }</td>
                    <td>${ htmlEncode(product.name) }</td>
                    <td class="numbers">${ htmlEncode(product.price) }</td>
                    <td class="numbers">${ htmlEncode(product.instock) }</td>
                    <td><span><img src="/static/images/${product.image}" style="width: 45px;"></td>
                    <td>
                        <button class="btn btn-secondary p-1 ps-3 pe-3" onclick="editProduct(${product._id})">Edit</button>&nbsp;
                        <button class="btn btn-danger p-1 ps-3 pe-3" onclick="editProduct(${product._id})">Delete</button>
                    </td>
                </tr>`;
                productsTable.find('tbody').append(template);
            }
        }

    });
};
