$(document).ready(function() {
    const table = $('#datatable-buttons').DataTable({
        lengthChange: false,
        pageLength: 50,
        buttons: ['copy', 'excel', 'pdf', 'print', 'colvis'],
    });

    table.buttons().container()
        .appendTo('#datatable-buttons_wrapper .col-md-6:eq(0)');
} );

