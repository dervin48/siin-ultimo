$(function () {
    $('input[name="birthdate"]').datetimepicker({
        useCurrent: false,
        format: 'YYYY-MM-DD',
        locale: 'es',
        keepOpen: false,
        maxDate: new Date()
    });

    $('.select2').select2({
        theme: 'bootstrap4',
        language: "es"
    });
});