$('#newWeather').click(function () {
    event.preventDefault();

    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        type: "GET",
        data: {
            'APPID': 'c8eac569cc2d3fdfcacf8e3d12ab728f',
            'q': 'portland'
        },
        success: function (d) {
            console.log(d.main.temp);
            console.log(d.weather[0].description);
        },
        error: function (d) {
            console.log(d);
        }
    });
});