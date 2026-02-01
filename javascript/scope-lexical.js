let globalVar = "I am global";

function outer() {
  let outerVar = "I am outer";

  function inner() {
    let innerVar = "I am inner";
    console.log(globalVar);
    console.log(outerVar);
    console.log(innerVar);
  }

  inner();
}

outer();
