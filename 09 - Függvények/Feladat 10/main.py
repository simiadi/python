from console import *
from mathFunctions import *

n1: float = getNumberInRangeFromConsole(0, 9)
n2: float = getNumberInRangeFromConsole(40, 50)
rndNumber: float = generateRandomNumberBetweenRange(n1, n2)
guess: int = guessRandomNumber(n1, n2, rndNumber)

printToConsole(guess)