print("A gasolina está R$ 4,30.")
pgaso=float(4.30)
litros=float(input("Quantor o senhor(a) que abastecer em reais: "))
resultado=float(litros / pgaso)
if resultado > 1:
    print("Você abastecera {:.2F}".format(resultado) , " litros." )
else:
    print("Você abastecera {:.2F}".format(resultado) , " litros." )

