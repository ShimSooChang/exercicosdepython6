salario=int(input("Qual é o seu salario mensal em reais: "))
despesas=int(input("De quanto são suas despesas mensais em reais: "))
meta=int(input("Qual é sua meta de dinheiro em reais: "))
D = salario - despesas
umAno=int(D * 12)
Q=int(meta / umAno)
print("Para atingir sua meta de dinheiro é necessario esperar" ,Q, "anos.")
