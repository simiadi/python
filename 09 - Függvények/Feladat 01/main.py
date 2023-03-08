from console import *
from mathFunctions import *

x: float = None
y: float = None
sumresult: float = None
extractionresult: float = None
multiplyresult: float = None
divisionresult: float = None

x = getNumberFromConsole()
y = getNumberFromConsole()

sumresult = sumOfTwoNumbers(x, y)
printToConsole(x, y, sumresult, "+")

extractionresult = extractionOfTwoNumbers(x, y)
printToConsole(x, y, extractionresult, "-")

multiplicationresult = multiplicationOfTwoNumbers(x, y)
printToConsole(x, y, multiplicationresult, "*")

divisionresult = divisionOfTwoNumbers(x, y)
printToConsole(x, y, divisionresult, "/")