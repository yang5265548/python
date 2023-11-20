  'use strict';
  const year = parseInt(prompt('please enter a year: '));
  const ans = leafOrNot(year);
  document.querySelector('#target').innerHTML = year + ans;
  function leafOrNot(year) {
    if (year % 4 === 0) {
      return ' is leaf year ';
    } else if (year % 100 === 0 && year % 400 === 0) {
      return ' is leaf year';
    } else {
      return ' is  not leaf year';
    }
  }
