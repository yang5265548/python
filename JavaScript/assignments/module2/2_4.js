'use strict';

let numArray = [];
while (true) {
  const number = parseInt(prompt('please enter a num'));
  if (number === 0) {
    break;
  } else {
    numArray.push(number);
  }
}
numArray.sort(function(a, b) {
  return a - b;
}).reverse();
for (let i = 0; i < numArray.length; i++) {
  console.log(numArray[i]);

}