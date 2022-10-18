var input_is_inventoried;

$(function () {
    input_is_inventoried = $('input[name="is_inventoried"]');

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('input[name="pvp"]')
        .TouchSpin({
            min: 0.01,
            max: 1000000,
            step: 0.01,
            decimals: 2,
            boostat: 5,
            verticalbuttons: true,
            maxboostedstep: 10,
            prefix: '$'
        })
        .on('keypress', function (e) {
            return validate_decimals($(this), e);
        });

    $('input[name="stock"]')
        .TouchSpin({
            min: 0,
            max: 1000000,
            step: 1,
            verticalbuttons: true,
        })
        .on('keypress', function (e) {
            return validate_form_text('numbers', e, null);
        });

    input_is_inventoried.on('change', function () {
        var container = $(this).parent().parent().find('input[name="stock"]').parent().parent();
        $(container).show();
        if (!this.checked) {
            $(container).hide();
        }
    });

    if ($('input[name="action"]').val() === 'edit') {
        input_is_inventoried.trigger('change');
    }

    // input_is_inventoried.removeClass();
});