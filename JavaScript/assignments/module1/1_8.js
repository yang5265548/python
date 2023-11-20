'use strict';
  const startYear = parseInt(prompt('please enter the start year:'));
  const endYear = parseInt(prompt('please enter the end year:'));
  let array = [];
  for (let i = startYear; i <= endYear; i++) {
    if (leafOrNot(i)) {
      array.push(i);
    }
  }
  // const ul = document.createElement('ul');
  const ul = document.querySelector('ul');
  for (let i = 0; i < array.length; i++) {

    const li = document.createElement('li');
    li.innerText = array[i];
    ul.appendChild(li);
    // console.log(array[i]);
  }

  function leafOrNot(year) {
    if (year % 4 === 0) {
      return true;
    } else return year % 100 === 0 && year % 400 === 0;
  }
