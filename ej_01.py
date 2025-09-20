precio = int(input("ingresa precio: "))
if precio >= 100:
    precio_final= precio*0.8
    print(f"precio final:{precio_final}con 20% descuento")
elif precio >= 50:
    precio_final=precio*0.9
    print(f"precio final es:{precio_final}con descuento 10%")
else:
    print(f"precio final: {precio} sin descuento")
