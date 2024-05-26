Algoritmo condicional_despensa
	Escribir "ingrese la cantidad de litros de leche de la compra:"
	Leer cantidad_leche
	Escribir "Ingrese 1 si el cliente es jubilado; Ingrese 2 si el cliente no es jubilado:"
	Leer cond_jubilado
	monto_sin_descuento<-cantidad_leche * 1000
	Si cantidad_leche <12 y cond_jubilado ==2 Entonces
		monto_final = monto_sin_descuento
	SiNo
				Si cantidad_leche >=12 y cantidad_leche <=24 y cond_jubilado ==2 Entonces
			monto_final = monto_sin_descuento * 0.90
		SiNo 
			Si cantidad_leche >=24 y cond_jubilado ==2 Entonces
				monto_final = monto_sin_descuento * 0.85
			SiNo 
				Si cantidad_leche < 12 y cond_jubilado ==1 Entonces
					monto_final = monto_sin_descuento * 0.90
				SiNo 
					Si cantidad_leche >=12 y cantidad_leche <=24 y cond_jubilado ==1 Entonces
						monto_final = monto_sin_descuento * 0.80
					SiNo monto_final = monto_sin_descuento * 0.75
						
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	Escribir "el monto a pagar es: " monto_final
	Escribir "el monto sin descuentos es:", monto_sin_descuento
FinAlgoritmo
