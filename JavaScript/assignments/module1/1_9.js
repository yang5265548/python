 'use strict';
  const num = parseInt(prompt('please enter the number:'));
  isPrime(num)
function isPrime(num) {
  let flag=true;
  if (num===1){
    document.querySelector('#target').innerHTML=num+' is not prime.';
  }else {
    for (let i = 2; i <Math.ceil(num/2); i++) {
        if(num%i===0){
          flag=false;
          break;
        }
    }
    if (flag){

      document.querySelector('#target').innerHTML=num+' is prime.';
    }else {

      document.querySelector('#target').innerHTML=num+' is not prime.';
    }
  }

}

