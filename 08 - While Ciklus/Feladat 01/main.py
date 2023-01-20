number: int = None
temp: str = None
isnumber: bool = False

while(number == None):
    print("Adjon meg egy számot", end="")
    temp = input()
    isNumber = isinstance(temp, (int, float))