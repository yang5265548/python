'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const sel=document.querySelector("#target");
for (let i=0;i<students.length;i++){
  let op=document.createElement("option");
  op.value=students[i]["id"];
  op.text=students[i]['name'];
  sel.appendChild(op)
}