'use strict';
let numArrary = [7, 5, 4, 3, 2, 8];
const evenArrary = even(numArrary);
console.log(numArrary);
console.log(evenArrary);

function even(numArrary) {
  let evenArray = [];
  for (let i = 0; i < numArrary.length; i++) {
    if (numArrary[i] % 2 === 0) {
      evenArray.push(numArrary[i]);
    }
  }
  return evenArray;
}