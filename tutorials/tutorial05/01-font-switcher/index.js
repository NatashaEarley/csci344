const makeBigger = () => {
   let myElement = document.querySelector("div.content");
   myElement.style.fontSize = "xx-large";
   let myHeader = document.querySelector("h1");
   myHeader.style.fontSize = "xxx-large";
};

const makeSmaller = () => {
   let myElement = document.querySelector("div.content");
   myElement.style.fontSize = "";
   let myHeader = document.querySelector("h1");
   myHeader.style.fontSize = "";
};