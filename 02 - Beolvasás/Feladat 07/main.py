from os import system

print("Adja meg a kedvenc autómárkájának a nevét: ", end="")
markanev: str = str(input())
print("Adja meg a modell nevét: ", end="")
modellnev: str = str(input())
print("Adja meg a típus nevét: ", end="")
tipusnev: str = str(input())
print("Adja meg hány köbcenti: ", end="")
kobcenti: int = int(input())
print("Adja meg a megjelenési évét: ", end="")
megjelenesiev: int = int(input())
system("cls")
print(f"Márka: {markanev} \nModell: {modellnev} \nTípus: {tipusnev} \nKöbcenti: {kobcenti} \nMegjelenési év: {megjelenesiev}")