"""
- Formulen un programa que:
i. A una variable se le asigne un mensaje motivador que incluya los nombres de todos los
integrantes. ¿Qué tipo de dato puede ser?
ii. Se asegure que todos su caracteres estén en mayúscula.
iii. Elabore una lista con cada palabra del string.
iv. Cada integrante del grupo debe reconocer en qué índice está su nombre.
v. Indique cuántas palabras tenía el string.
vi. Imprima una tupla con todas las palabras del string.

vii. ¿Con qué función podrían obtener el mensaje por teclado al ejecutar el programa?
Implementarlo!.
"""

saludarIntegrantes = "Hola todos serán grandes programadores, y entre los mejores están: Adolfo, Alan, Cristobal, Daniela, Jesus, Xabier." # Debe ser tipo string ya que es un texto
saludarIntegrantes = saludarIntegrantes.upper()

listaSaludo = saludarIntegrantes.replace(',','').replace('.','').split()
#['HOLA', 'TODOS', 'SER�N', 'GRANDES', 'PROGRAMADORES', 'Y', 'ENTRE', 'LOS', 'MEJORES', 'EST�N:', 'ADOLFO', 'ALAN', 'CRISTOBAL', 'DANIELA', 'JESUS', 'XABIER']

print(listaSaludo)

#Adolfo - indice 10
#Alan - indice 11
#Cristobal - indice 12
#Daniela - indice 13
#Jesus - indice 14
#Xabier - indice 15

cantidadPalabrasEnElTexto = len(listaSaludo)
print(cantidadPalabrasEnElTexto) #16

tuplaSaludo = tuple(listaSaludo)
print(tuplaSaludo)
#('HOLA', 'TODOS', 'SER�N', 'GRANDES', 'PROGRAMADORES', 'Y', 'ENTRE', 'LOS', 'MEJORES', 'EST�N:', 'ADOLFO', 'ALAN', 'CRISTOBAL', 'DANIELA', 'JESUS', 'XABIER')



superSaludo = input("Inregesa un saludo: ")
nombreIntegrantes = input('Ingrese el nombre de la persona a saludar: ')

print(f"{superSaludo} {nombreIntegrantes}")

megaSaludo = input("Inregesa un megaSaludo: ")
integrantes = []
salir = "1"
hiperSaludo = megaSaludo

while salir == "1":
    integrantes.append(input("Ingrese un integrante a saludar: "))
    salir = (input("Si dese agregar otro integrate a saludar presione 1, sino presione 0: "))

for nombre in integrantes:
    print(f'{megaSaludo} {nombre}')
    hiperSaludo += " "+ nombre

print(hiperSaludo)