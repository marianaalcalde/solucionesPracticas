precio_sin_iva = float(input("ingrese el  precio sin iva: "))
porcentaje_iva = float(input("ingrese el porcentaje de iva aplicable:"))
precio_con_iva = precio_sin_iva * (1 + (porcentaje_iva / 100))
print("el precio de lista es: ", precio_con_iva)
