function change_rarity_html(element) {
    $.post('{{ url_for("user.change_char_rarity") }}')
    .done(function(changed) {
        $(element).text(changed['rarity'])
    }).fail(function() {
     $(element).text("Error")
    });
}

