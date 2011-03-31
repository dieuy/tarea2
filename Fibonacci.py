# Programa que muestra en pantalla la sucesion de Fibonacci.py

def fibonacci (x) :
	a,b = 0,1
	if x < 1 :
		print "El numero tiene que ser un natural"
	else :
		for i in range(0,x):  
     			print b  
     			a,b = b,a+b 

x = int(raw_input("Ingrese un numero: "))
fibonacci(x)
