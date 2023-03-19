print("\n\tCalculadora")
print("Que operacion deceas realizar")
print("1)Sumar\n2)restar\n3)multiplicar\n4)dividir")

elige = int(input("escoja una opcion: "))
if elige==1:
    print("Elija los numeros que desea sumar")
    numero1 = float(input("primera cantidad:"))
    numero2 = float(input("segunda cantidad: "))
    numero3=numero1 + numero2
    print("Su suma es ")
    print(numero3)
if elige==2:
    print("Elija los numeros que desea restar")
    numero1 = float(input("primera cantidad:"))
    numero2 = float(input("segunda cantidad:"))
    numero3=numero1 - numero2
    print("Su resta es ")
    print(numero3)
if elige==3:
    print("La multiplicacion es")
    numero1 = float(input("Primera cantidad "))
    numero2 = float(input("Segundo numero "))
    print("Su multiplicacion es\t ")
    numero3 = numero1*numero2
    print(numero3)
if elige==4:
    numero1 = float(input("Numerador: "))
    numero2 = float(input("Denominador: "))
    if numero2!=0:
     print("El resultado de su divicion es el siguiente:\t")
     numero3=numero1/numero2
     print(numero3)
     print("\t")
    else:
       print("No se puede hacer esta operacion\nporque cuando tiende a cero su denominador\nla cifra no esta definida\n")
