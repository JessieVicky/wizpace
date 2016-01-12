$(document).ready(function() {
    $("#id_country").select2({
        placeholder: 'Select a country',
    });

    $("#id_city").select2({
        placeholder: 'Select a city',
        // disabled: true,
        ajax: {
            url: "./search_city/",
            delay: 300,
            dataType: 'json',
            cache: true,
            data: function (params) {
                var selects = document.getElementById('id_country');
                var selectedText = selects.options[selects.selectedIndex].text;
                return {
                    q: params.term, // search term
                    country: selectedText,
                };
            },
            processResults: function (data) {
                var myResults = [];
                $.each(data, function(index, item) {
                    myResults.push({
                        'id': item.id,
                        'text': item.name
                    });
                });
                return {
                    results: myResults
                };
            },
            formatNoResults: function () {
                return "No results found.";
            },
            formatAjaxError: function () {
                return "No connection to the server";
            },
        },
        escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
        minimumInputLength: 1,
    });

});