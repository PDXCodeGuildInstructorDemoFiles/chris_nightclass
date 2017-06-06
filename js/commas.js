'use strict';

function reverseString(str) {
    // Step 1. Use the split() method to return a new array
    var splitString = str.split(""); // var splitString = "hello".split("");
    // ["h", "e", "l", "l", "o"]

    // Step 2. Use the reverse() method to reverse the new created array
    var reverseArray = splitString.reverse(); // var reverseArray = ["h", "e", "l", "l", "o"].reverse();
    // ["o", "l", "l", "e", "h"]

    // Step 3. Use the join() method to join all elements of the array into a string
    var joinArray = reverseArray.join(""); // var joinArray = ["o", "l", "l", "e", "h"].join("");
    // "olleh"

    //Step 4. Return the reversed string
    return joinArray; // "olleh"
}


document.getElementById('getNumber').addEventListener('click', function() {
    var number = document.getElementById('number').value;
    var numberReversed = reverseString(number);
    var threeNumberArray = [];

    for (var i = 0; i < numberReversed.length; i+=3) {
        var threeNumber = '';

        if (numberReversed[i] !== undefined){
            threeNumber += numberReversed[i];
        }

        if (numberReversed[i+1] !== undefined){
            threeNumber += numberReversed[i+1];
        }

        if (numberReversed[i+2] !== undefined){
            threeNumber += numberReversed[i+2];
        }

        threeNumberArray.push(threeNumber);
    }

    var threeNumberArrayJoined = threeNumberArray.join(',');
    var finalString = reverseString(threeNumberArrayJoined);
    // var stringToNumber = parseInt(number);
    // var numberComma = stringToNumber.toLocaleString();
    document.getElementById('message').innerHTML = finalString;
});
