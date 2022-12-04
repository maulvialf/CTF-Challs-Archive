$(document).ready(() => {
    loadexports();
});

const loadexports = async () => {
    await fetch(`/api/tracker/exports`, {
        method: 'GET',
        credentials: 'include'
    })
    .then((response) => response.json()
        .then((data) => {
            for (let map_export of data) {
                populateTable(map_export);
            }
        }))
    .catch((error) => {
        console.error(error);
    });
}

const populateTable = (map_export) => {
    if (map_export.export_map == null) {
        map_link = 'Not Exported Yet';
    }
    else {
        map_link = `<a target="_blank" href="/static/exports/${map_export.export_map}">${map_export.export_map}</a>`
    }

    let tabHTML = `<tr>
    <td>${map_export.uuid}</td>
    <td>${map_export.email}</td>
    <td>${map_link}</td>
    </tr>`
    $('#export-tbody').append(tabHTML);

}


