//DataTable
$(document).ready(function () {
    $('#dataTablePersonal').DataTable({
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": " _START_ al _END_ de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sSearch": "Buscar:",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                //"sNext": "Siguiente",
                //"sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        "aLengthMenu": [[10, 25, 30, -1], [10, 25, 30, "All"]],
        "iDisplayLength": 10,
        "columnDefs": [
            { "orderable": false, "targets": [0, 1, 4, 5, 6, 8, 9] }, // Deshabilita el orden en las columnas 
            { "className": "dt-center", "targets": "_all" }
        ],
        "responsive": "True",
        "dom": "<'row'<'col-md-2'l><'col-md-6 text-md-center'B><'col-md-4 text-md-end'f>>rt<'row'<'col-md-2'i><'col-md-6'><'col-md-4 text-md-end'p>>",
        "buttons": [
            {
                extend: "excelHtml5",
                text: "<i class='fa-solid fa-file-csv'></i>",
                tittleAttr: "Exportar a Excel",
                className: "btn btn-success",
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5, 6, 7]
                }
            },
            {
                extend: "pdfHtml5",
                text: "<i class='fa-solid fa-file-pdf'></i>",
                tittleAttr: "Exportar a pdf",
                className: "btn btn-danger",
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5, 6, 7]
                }
            },
            {
                extend: "print",
                text: "<i class='fa fa-print'></i>",
                tittleAttr: "Imprimir",
                className: "btn btn-info",
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5, 6, 7]
                }
            }
        ],
    });
});
