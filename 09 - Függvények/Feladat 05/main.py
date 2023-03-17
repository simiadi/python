from console import *
from stringFunctions import *

n1: str = None
n2: str = None
result: str = None

n1 = getWordFromConsole()
n2 = getWordFromConsole()
result = getSameLetters(n1, n2)
printToConsole(result)