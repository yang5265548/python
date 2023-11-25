'use strict';
const maxsides = parseInt(prompt('please enter the maxsides of the dice: '));
let numArray = [];
while (true) {
  const num = roll();
  if (num === maxsides) {
    numArray.push(num);
    break;
  } else {
    numArray.push(num);
  }
}
const ul = document.querySelector('#target');
for (let i = 0; i < numArray.length; i++) {
  const li = document.createElement('li');
  li.innerText = numArray[i];
  ul.appendChild(li);
}

function roll() {
  return Math.floor(Math.random() * maxsides + 1);
}
