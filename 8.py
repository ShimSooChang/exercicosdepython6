salario=float(input("Qual é o seu salario mensal em reais: "))
despesas=float(input("De quanto são suas despesas mensais em reais: "))
meta=int(input("Qual é sua meta de dinheiro em reais: "))
D = salario - despesas
umAno=int(D * 12)
Q=float(meta / umAno)
print("Para atingir sua meta de dinheiro é necessario esperar {:.2F}".format(Q), "anos.")
