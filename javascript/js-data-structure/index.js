// const averageTemp = [];
// console.log(averageTemp);

// averageTemp[0] = 31.9;

// console.log(averageTemp);

// const daysOfWeek = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];

// for (let index = 0; index < daysOfWeek.length; index++) {
//   const element = daysOfWeek[index];
//   console.log(element)
// }

// const fibonacci = [];
// fibonacci[1] = 1;
// fibonacci[2] = 1;

// for (let i = 3; i < 20; i++) {
//   fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
// }

// for (let i = 0; i < fibonacci.length; i++) {
//   console.log(fibonacci[i]);
// }

let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
// console.log(numbers);
// numbers[numbers.length] = 10;
// console.log(numbers);
/* o numbers.lenght é igual a 10, então o
numbers na posição 10 vai ser igual a 10  */

// numbers.push(11, 12, 13);
// console.log(numbers);

Array.prototype.insertFirstPosition = function(value) {
 for (let i = this.length; i >= 0; i--) {
  this[i] = this[i - 1]
 }

 this[0] = value
}

numbers.insertFirstPosition(-1)