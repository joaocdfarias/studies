const defaultResult = 0
let currentResult = defaultResult

function add(number1, number2) {
  const result = number1 + number2
  return result
}

currentResult = add(10, 4)

let calculationDescription = `(${defaultResult} + 10) * 3 / 2 - 1`

outputResult(currentResult, calculationDescription)
