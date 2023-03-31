from console import *
from mathFunctions import *

value: float = getValueFromConsole()
currency: str = getCurrencyFromConsole()
result: float = convertCurrency(value, currency)
result2: float = convertCurrency(value, "EUR")

printToConsole(result, result2, currency)