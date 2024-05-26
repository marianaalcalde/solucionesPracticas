Algoritmo calcular_iva_alicuotas
	Escribir "ingrese el precio sin iva: "
	Leer precio_sin_iva
	Escribir "ingrese el porcentaje de iva aplicable:"
	Leer porcentaje_iva
	precio_con_iva<-precio_sin_iva * (1 + (porcentaje_iva/100))
	Escribir "el precio de lista es: " precio_con_iva
	
FinAlgoritmo
