  'use strict';
    const ans=confirm('Should I calculate the square root?')
    if (ans===true){
      const num=parseInt(prompt("please enter the num: "))
      if (num<0){
        document.querySelector('#target').innerHTML='The square root of a negative number is not defined';
      }else {
        const squa=Math.sqrt(num);
        document.querySelector('#target').innerHTML='the square root of  '+num+' is '+squa;
      }

    }else {
      document.querySelector('#target').innerHTML='The square root is not calculated.';
    }

