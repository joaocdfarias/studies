// Those variables are defined in global scope
const defaultResult = 0
let currentResult = defaultResult

function add(number1, number2) {
  // This variable is defined in function scope
  const result = number1 + number2
  alert(result)
}

add(10, 4)

currentResult = ((currentResult + 10) * 3) / 2 - 1

let calculationDescription = `(${defaultResult} + 10) * 3 / 2 - 1`

outputResult(currentResult, calculationDescription)
