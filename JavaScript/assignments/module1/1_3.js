    'use strict'
     const num1 =parseInt(prompt("please enter the first num:"))
     const num2 =parseInt(prompt("please enter the second num:"))
     const num3 =parseInt(prompt("please enter the third num:"))
    const sum=num1+num2+num3;
    const product=num1*num2*num3;
    const ave=sum/3;
     document.querySelector('#target').innerHTML='sum: '+sum+' product: '+product+' average: '+ave;