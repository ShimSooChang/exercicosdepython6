VB=int(input("Qual o valor do boleto: "))
Dias=int(input("Quantos dias de atraso: "))
Juros=int(input("Qual o percentual de juros: "))
Cal=(VB*Juros/100)
NV= VB + Cal * Dias
print("O novo valor do boleto é de ",NV, "reais." )