from console import *
from mathFunctions import *

x: float = None
y: float = None
sumresult: float = None
kivonasresult: float = None
szorzasresult: float = None
osztasresult: float = None

x = getNumberFromConsole()
y = getNumberFromConsole()

sumresult = sumOfTwoNumbers(x, y)
printToConsole(x, y, sumresult, "+")

kivonasresult = sumOfTwoNumbers(x, y)
printToConsole(x, y, kivonasresult, "-")

szorzasresult = sumOfTwoNumbers(x, y)
printToConsole(x, y, szorzasresult, "*")

osztasresult = sumOfTwoNumbers(x, y)
printToConsole(x, y, osztasresult, "/")