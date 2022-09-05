const defaultResult = 0
let currentResult = defaultResult

function add() {
  currentResult = currentResult + Number(userInput.value)
  outputResult(currentResult, '')
}

addBtn.addEventListener('click', add)
