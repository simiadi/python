from console import *
from mathFunctions import *

x1: float = getXFromConsole()
y1: float = getYFromConsole()
x2: float = getXFromConsole()
y2: float = getYFromConsole()

distance: float = getDistanceBetweenCoordinates(x1, x2, y1, y2)
printToConsole(distance)