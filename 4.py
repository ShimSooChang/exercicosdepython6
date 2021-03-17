print("A gasolina está R$ 4,30.")
pgaso=float(4.30)
litros=int(input("Quantor o senhor(a) que abastecer em reais: "))
resultado= litros // pgaso
if resultado > 1:
    print("Você abastecera" ,resultado, "litros." )
else:
    print("Você abastecera" ,resultado, "litro." )

