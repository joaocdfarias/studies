const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const isEven = (x) => x % 2 === 0;

console.log('Every => ', numbers.every(isEven));
console.log('Some => ', numbers.some(isEven));
numbers.forEach((x) => console.log(isEven(x)));

// Every, some e forEach irão iterar a array numbers

for (const number of numbers) {
  console.log(number % 2 === 0 ? 'even' : 'odd');
}

let iterator = numbers[Symbol.iterator]();
console.log(iterator.next().value);
console.log(iterator.next().value);
console.log(iterator.next().value);
