print("Hola soy un cambio!")
print("Hola maestra soy belen :)")
def areaCuadrado():
  lado=int(input("Capture el lado: "))
  area=lado*lado
  print("El area es = "+str(area))
  perimetro=lado*4
  print("El perimetro es = "+str(perimetro))

def areaTriangulo():
  base=int(input("Ingresa la base"))
  altura=int(input("Ingresa la altura"))
  area=(base*altura)/2
  perimetro=base*3
  print("El area del triangulo es = "+str(area))
  print("El area del perimetro es = "+str(perimetro))


print("Calcula areas y perimetros")
print("Opciones: ")
print("1. Cuadrado")
print("2. Triangulo")
print("3. Circulo")

"""
figura1= "1. cuadrado"
print(figura1)

figura2="2. triangulo"
print(figura2)
"""

numero=int(input("Ingresa el numero de la opcion a elegir"))

if numero==1:
  areaCuadrado()
elif numero==2:
  areaTriangulo()  





 
