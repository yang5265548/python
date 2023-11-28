function changePic(){
  const pic=document.querySelector("#target")
  pic.src="img/picB.jpg"
  console.log("fun1")
}
function changeBack(){
    const pic=document.querySelector("#target")
  pic.src="img/picA.jpg"
  console.log("fun2")
}
const p=document.querySelector("#trigger")
p.addEventListener("mouseenter",changePic);
p.addEventListener("mouseleave",changeBack);