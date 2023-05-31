# En base al contexto: Piensa en una aplicación web que busque solucionar una problemática.
# Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
# Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
# Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
# Ahora piensa en tres de ellos. Buscalos en la lista con el método adecuado.
# ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa
# manualmente su nombre? ¿Cómo solucionarías este problema?
# Convierte tu string en una lista, en la cual cada elemento es un usuario.
# Imprime en pantalla la cantidad usuarios que tiene tu aplicación.
# Imprimer en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes
# utilizar para realizar esto?

users = {
    "xabi": "xabi123", 
    "alan": "alan123", 
    "cristobal": "cristobal123", 
    "jesus": "jesus123", 
    "daniela": "dani123", 
    "andres": "andres123",
    "alonso": "alonso123"
}

print("Bienvenido al registro de Usuario")
option = input("Ingrese 0 para iniciar sesion o presione cualquier tecla para buscar usuario: ")

if option == "0":
    user=input("ingrese su nombre de usuario: ")
    if user in users:
        print("usuario ya existe")
        exit()
    contrasena=input("ingrese una contraseña: ")
    users[user]= contrasena
print("Bienvenido al inicio de sesion")

user=input("ingrese su usuario: ")
if user in users:
    contrasena=input("ingrese una contraseña: ")
    if contrasena == users[user]:
        print(f"Bienvenido {user}")
    else: 
        print("contraseña incorrecta")
else:
    print("usuario no existe")