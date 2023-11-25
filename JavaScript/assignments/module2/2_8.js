'use strict';
let nameArray = ['young', 'helen', 'kobe', 'james'];
const names = concat(nameArray);
document.querySelector('#target').innerHTML = names;

function concat(nameArrary) {
  let names = '';
  for (let i = 0; i < nameArrary.length; i++) {
    names = names + nameArrary[i];
  }
  return names;
}