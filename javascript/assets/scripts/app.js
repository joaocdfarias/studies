const defaultResult = 0
let currentResult = defaultResult

currentResult = add(10, 4)

let calculationDescription = `(${defaultResult} + 10) * 3 / 2 - 1`

outputResult(currentResult, calculationDescription)

// I can move the function to the bottom because JS pull functions to the top of the code
function add(number1, number2) {
  const result = number1 + number2
  return result
}
