"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros 
descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
"""

cantidad_leche = int(input("ingrese la cantidad de litros de leche de la compra:"))
cond_jubilado = int(input("Ingrese 1 si el cliente es jubilado; Ingrese 2 si el cliente no es jubilado:"))
monto_sin_descuento = cantidad_leche * 1000
if cantidad_leche < 12 and cond_jubilado ==2:
    monto_final = monto_sin_descuento
elif cantidad_leche >=12 and cantidad_leche <=24 and cond_jubilado ==2:
    monto_final = monto_sin_descuento * 0.90
elif cantidad_leche >=24 and cond_jubilado ==2:
    monto_final = monto_sin_descuento * 0.85
elif cantidad_leche < 12 and cond_jubilado ==1:
    monto_final = monto_sin_descuento * 0.90
elif cantidad_leche >=12 and cantidad_leche <=24 and cond_jubilado ==1:
    monto_final = monto_sin_descuento * 0.80
else: monto_final = monto_sin_descuento * 0.75
print ("el monto a pagar es: ", monto_final)
print ("el monto sin descuentos es:", monto_sin_descuento)
