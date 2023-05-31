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

def iniciosesion():
        user=input("Ingrese su nombre de usuario: ")
        if user in users:
            contrasena=input("Ingrese su Contraseña: ")
            if contrasena ==users[user]:
                print(f"Bienvenido {user} nos alegra verte de vuelta!!")
            else:
                volver_menu()
        else:
            print("usuario no encontrado")
            volver_menu()

cantidad_de_usuario = len(users)

def consultausuario():
        usuarios= list(users)
        print(usuarios)
        print(f"Cantidad de usuarios registrados: {cantidad_de_usuario} ")

def volver_menu():
        print("¿Desea volver al inicio de sesion? ")
        volver=input("Ingrese 0 para volver al menu de inicio de sesion o cualquier tecla para Finalizar: ")
        if volver == "0":
            iniciosesion()
        else:
            print("Esperamos verte pronto...")

print("Bienvenido al menu de inicio de sesion")
option = input("Ingrese 0 para iniciar sesion o presione cualquier tecla para buscar usuario: ")

if option == "0":
    iniciosesion()
else:
    consultausuario()
    volver_menu()


