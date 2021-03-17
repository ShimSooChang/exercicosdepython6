#informar achar o volume  de uma lata de oleo usando formula 3.14*(R*R)*h

Raio=float(input("Insira o valor de raio:"))
h=int(input("Insira o valor da altura:"))
pi=int(3.14)
Rbig = Raio * Raio
Volume= pi * Rbig * h
if Volume > 1:
    print("O volume cúbico desta lata de óleo é",Volume, "litros") 
else:
     print("O volume cúbico desta lata de óleo é",Volume, "litro") 
