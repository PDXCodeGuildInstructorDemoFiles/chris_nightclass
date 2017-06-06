'use strict';

var names = [
    'Tab',
    'Chase',
    'Larry',
    'Ian',
    'Joe',
    'Malcolm',
    'Mike'
];

var greet = function (n) {
    var color;
    if (n === 'Chris') {
        color = '#3723e0'
    } else if (n === 'Katie') {
        color = '#E0200D'
    } else {
        color = "#24e016"
    }
    var message = document.getElementById('message');
    message.innerHTML = "hello " + n + '!';
    message.style.color = color;
};

document.getElementById('getName').addEventListener('click', function () {
    var name = document.getElementById('name').value;
    greet(name);
});


function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

// names = shuffle(names);
//
// for (var i = 0; i < names.length; i++){
//     var ol = document.getElementById('student_order');
//     var li = document.createElement("li");
//     li.appendChild(document.createTextNode(names[i]));
//     ol.appendChild(li);
// }

var fruitToPrice = {"apple": 0.99};
console.log(fruitToPrice.apple * 7);

var thing = [1, 2, 3];
thing.forEach(function(i) {
    console.log(i);
});