#Devuelve los numeros primos del orden natural hasta n

def es_primo (x) :
    cont = 2
    orden = True
    while (orden and (x <> cont)) :
        if (x % cont == 0) :
            orden = False
        else :
            cont += 1
    return orden

n = raw_input("Ingrese un valor : ")

print "Los numeros primos del 1 al " + n + " son : "
for i in range(2,int(n)):
    if es_primo(i): 
        print str(i)    
