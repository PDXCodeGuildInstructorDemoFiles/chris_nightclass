'use strict';

$('#getColor').click(function () {
    event.preventDefault();
    var color = $('#color').val();
    $('body').css('background-color', color);
    $('#message').html(color);
});


$('#addToDo').click(function () {
    event.preventDefault();
    var input = prompt('Enter an item');
    $('#items').append('<li>' + input + '</li>');
});

$.each([], function () {

});