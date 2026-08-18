import math 

print("CÁLCULO DE VOLÚMENES")
print("1. Prisma")
print("2. Piramide")
print("3. Cono truncado")
print("4. Cilindro")

decision = int(input("\nIngrese el numero de la opcion que desea: "))

if decision==1: 
    areaBase = float(input("Ingrese el área de la base: "))
    altura = float(input("ingrese la altura: "))
    
    volumen = areaBase * altura
    
    print("El volumen del prisma es: ", volumen)
    
elif decision==2:
    areaBase = float(input("Ingrese el área de la base: "))
    altura = float(input("ingrese la altura: "))
        
    volumen = (areaBase * altura)/3        
    
    print("El volumen de la piramide es: ", volumen)
    
elif decision==3:
    radioMayor = float(input("Ingrese el radio mayor: "))
    radioMenor = float(input("Ingrese el radio menor: "))
    altura = float(input("Ingrese la altura: "))
    
    volumen = ((math.pi * altura)/3) * (radioMayor**2 + (radioMayor*radioMenor) + radioMenor**2)
    
    print("El volumen del cono truncado es: ", volumen)
    
elif decision==4:
    radio = float(input("Ingrese el radio: "))
    altura = float(input("Ingrese la altura: "))
    
    volumen = math.pi * (radio**2) * altura
    
    print("El volumen del cilindro es: ", volumen)
    
else: 
    print("Opcion invalida")
    
