'use strict';
let num = parseInt(prompt('please enter the num of candidates: '));
let candidatArrays = [];
for (let i = 1; i <= num; i++) {
  let jsonArray = {};
  jsonArray.name = prompt('please enter the name of candindate ' + i);
  jsonArray.vote = 0;
  candidatArrays.push(jsonArray);
}

let numVoters = parseInt(prompt('please enter the num of vorters: '));
for (let i = 0; i < numVoters; i++) {
  let voteName = prompt('please enter the candidate name: ');
  if (voteName === NaN) {
    console.log('enter a empty vote');
  } else {
    for (let j = 0; j < candidatArrays.length; j++) {
      if (candidatArrays[j].name === voteName) {
        candidatArrays[j].vote += 1;
        break;
      }
    }
  }
}
candidatArrays.sort(function(a, b) {
  return b.vote - a.vote;
});
console.log('the winner is ' + candidatArrays[0].name + ' with ' +
    candidatArrays[0].vote + ' votes.');
console.log('results:');
for (let i = 0; i < candidatArrays.length; i++) {
  console.log(
      candidatArrays[i].name + ' : ' + candidatArrays[i].vote + ' votes');
}
