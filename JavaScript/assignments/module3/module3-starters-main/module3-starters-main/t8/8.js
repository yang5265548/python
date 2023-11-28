function caclt() {
  const num1 = parseFloat(document.querySelector('#num1').value);
  const num2 = parseFloat(document.querySelector('#num2').value);
  const selectElement=document.querySelector("#operation")
  // const selectOption=selectElement.options[selectElement.selectedIndex]
  // const selectValue=selectOption.value
  const value=selectElement.value
  let result;
  switch (value) {
    case "add":
      result=num1+num2;
      break;
    case "sub":
      result=num1-num2;
      break;
    case "multi":
      result=num1*num2;
      break;
    case "div":
      if (num2==0){
        alert("the num2 cant be 0~~")
      }else {
        result=num1/num2;
      }

  }
  // console.log(value)
  // console.log(num1);
  // console.log(num2);
  const p=document.querySelector("#result")
  p.innerHTML=result
}

const btn = document.querySelector('#start');
btn.addEventListener('click', caclt);

