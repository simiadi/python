a: int = None
b: int = None

while True:
    try:
        print("Adjon meg egy egész számot: ", end="")
        a = int(input())
        break
    except:
        print("That's not a valid option!")

print("Adjon meg egy egész számot: ", end="")
a = input()

print("Adjon meg mégegy egész számot: ", end="")
b = input()

def osszeadas(a: int, b: int) -> int:
    eredmeny: int = a + b
    return eredmeny
def kivonas(a: int, b: int) -> int:
    eredmeny: int = a - b
    return eredmeny
def szorzas(a: int, b: int) -> int:
    eredmeny: int = a * b
    return eredmeny
def osztas(a: int, b: int) -> int:
    eredmeny: int = a / b
    return eredmeny