let currentResult = 0

currentResult = currentResult + 10
console.log('1', currentResult)
// In this case you assigning the previous value + 10
// So currentResult = 0 + 10 = 10
// If we do this again currentResult = 10 + 10 = 20
currentResult = currentResult + 10
console.log('2', currentResult)
// Basically, currentResult is overwritten by itself + 10

outputResult(currentResult, '')
