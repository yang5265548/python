'use strict';
const num = parseInt(prompt('please enter the num of participants:'));
let nameArray = [];
for (let i = 0; i < num; i++) {
  nameArray.push(prompt('please enter the name:'));
}
nameArray.sort();
const ol = document.querySelector('#target');
for (let i = 0; i < nameArray.length; i++) {
  const li = document.createElement('li');
  li.innerText = nameArray[i];
  ol.appendChild(li);
}
