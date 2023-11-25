let numarray = [];
for (let i = 0; i < 5; i++) {
  numarray.push(prompt('please enter a num: '));
}
for (let i = numarray.length - 1; i >= 0; i--) {
  console.log(numarray[i]);

}
