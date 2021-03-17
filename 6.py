#informar achar o volume  de uma lata de oleo usando formula 3.14*(R*R)*h

Raio=float(input("Insira o valor de raio:"))
h=float(input("Insira o valor da altura:"))
pi=float(3.14)
Rbig = Raio * Raio
Volume=float(pi * Rbig * h)
if Volume > 1:
    print("O volume cúbico desta lata de óleo é de {:.2F}".format(Volume), "litros") 
else:
     print("O volume cúbico desta lata de óleo é de {:.2F}".format(Volume), "litro") 
