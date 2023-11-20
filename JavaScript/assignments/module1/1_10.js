 'use strict';
  const disnum = parseInt(prompt('please enter the num of dics:'));
  const innum = parseInt(prompt('please enter the eye num :'));
  rolldics(disnum,innum);

  function rolldics(disnum,innum){
    let num=0;
    let i=0;
    while (i<100000){
      let sum=0;
      for (let j=0;j<=disnum;j++){
        sum+=Math.floor(Math.random() * 6 + 1);
      }
      if (sum===innum){
        num++;
      }
      i++;
    }
    console.log(num)
   let prop=(num/1000).toFixed(2);

    document.querySelector('#target').innerHTML='Probability to get sum '+innum +' with '+disnum+' dice is '+prop+'%.'

  }
