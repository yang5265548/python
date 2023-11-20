  'use strict';
  const times = parseInt(prompt('please enter the times of rolls:'));
  let sum = 0;
  for (let i = 0; i < times; i++) {

    sum += Math.floor(Math.random() * 6 + 1);

  }
  document.querySelector('#target').innerHTML = 'the sum is ' + sum;
