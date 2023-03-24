from console import *
from convertFunctions import *

celsius: float = getValueFromConsole()
unit: str = getUnitFromConsole()
result: str = convertCelsius(celsius, unit)
printToConsole(result, celsius, unit)