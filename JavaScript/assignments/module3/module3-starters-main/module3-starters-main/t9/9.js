function calcu(){
  const str=document.querySelector("#calculation").value
  console.log(str)
  let result;
  // const an=str.includes("/")
  // console.log(an)
  if(str.includes("+")){
    const array=str.split("+");
    result=parseInt(array[0])+parseInt(array[1]);
  }else if (str.includes("-")){
    const array=str.split("-");
    result=parseInt(array[0])-parseInt(array[1]);
  }else if (str.includes("*")){
    const array=str.split("*");
    result=parseInt(array[0])*parseInt(array[1]);
  }else if (str.includes("/")){
    const array=str.split("/");
    if (array[1]==0){
      alert("the num2 cant be 0~~")
    }else {
     result=parseInt(array[0])/parseInt(array[1]);
    }

  }
  const  p=document.querySelector("#result");
  p.innerHTML=result;
}
const cal=document.querySelector("#start");
cal.addEventListener("click",calcu)