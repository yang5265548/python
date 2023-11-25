'use strict';
// const num=parseInt(prompt("please enter the num of participants:"));
let nameArray = [];
for (let i = 0; i < 6; i++) {
  nameArray.push(prompt('please enter the dog\'s name:'));
}
nameArray.sort().reverse();
const ul = document.querySelector('#target');
for (let i = 0; i < nameArray.length; i++) {
  const li = document.createElement('li');
  li.innerText = nameArray[i];
  ul.appendChild(li);
}