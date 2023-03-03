from console import *
from mathFunctions import *

x: float = None
y: float = None
result: float = None

x = getNumberFromConsole()
y = getNumberFromConsole()

result = sumOfTwoNumbers(x, y)
printToConsole(x, y, result, "+")