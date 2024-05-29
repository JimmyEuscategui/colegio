//DataTable
$(document).ready(function () {
    $('#dataTableAcudiente').DataTable({
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
            { "orderable": false, "targets": [2, 3, 4, 5, 6] }, // Deshabilita el orden en las columnas 0, 1, 3, 4, 5, 6 y 8
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
                    columns: [0, 1, 2, 3, 4, 5]
                }
            },
            {
                extend: "pdfHtml5",
                text: "<i class='fa-solid fa-file-pdf'></i>",
                tittleAttr: "Exportar a pdf",
                className: "btn btn-danger",
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            },
            {
                extend: "print",
                text: "<i class='fa fa-print'></i>",
                tittleAttr: "Imprimir",
                className: "btn btn-info",
                exportOptions: {
                    columns: [0, 1, 2, 3, 4, 5]
                }
            }
        ],
    });
});

//SweetAlert2 eliminar estudiante
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.eliminar-estudiante').forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const url = this.getAttribute('href');
      Swal.fire({
        title: '¿Estás seguro?',
        text: 'No podrás revertir esto',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminarlo!'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = url;
        }
      });
    });
  });
});