'use strict';
const names = ['John', 'Paul', 'Jones'];
let sublist='';
for (let i=0;i<names.length;i++){
  const velue=names[i]
  sublist+="<li>" +velue +"</li>"
}
document.querySelector("#target").innerHTML=sublist