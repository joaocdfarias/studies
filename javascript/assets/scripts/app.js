const defaultResult = 0
// We're not asigning a new value to defaultResult, we're copying
// the value to currentResult
let currentResult = defaultResult

currentResult = ((currentResult + 10) * 3) / 2 - 1

let calculationDescription = `(${defaultResult} + 10) * 3 / 2 - 1`

outputResult(currentResult, calculationDescription)
