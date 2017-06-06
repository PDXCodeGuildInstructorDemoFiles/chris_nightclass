// http://api.icndb.com/jokes/random


$('#newJoke').click(function () {
    event.preventDefault();

    $.ajax({
        url: "http://api.icndb.com/jokes/random",
        type: "POST",
        success: function (data) {
            $('#joke').html(data.value.joke);
            // console.log(data.value.joke)
        },
        error: function (data) {
            console.log(data)
        }
    });
});