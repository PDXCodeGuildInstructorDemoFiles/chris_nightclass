"use strict";

document.getElementById('getNumber').addEventListener('click', function () {
    var str = document.getElementById('number').value;
    var decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    var roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    var total = 0;

    for (var i = 0; i <= decimal.length; i++) {
        while (str.indexOf(roman[i]) === 0) {
            total += decimal[i];
            str = str.replace(roman[i], '');
        }
    }

    document.getElementById('message').innerHTML = total;
});