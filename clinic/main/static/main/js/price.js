function toggleTable(tableId) {
    var tables = document.getElementsByClassName('table-content');

    for (var i = 0; i < tables.length; i++) {
        if (tables[i].id === tableId) {
            continue;
        }
        tables[i].style.display = 'none';
    }

    var tableContent = document.getElementById(tableId);
    if (tableContent.style.display === 'none') {
        tableContent.style.display = 'table';
    } else {
        tableContent.style.display = 'none';
    }
}
