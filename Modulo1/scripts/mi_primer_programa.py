# .py -> extensión de python
# con esto vscode se da cuenta que trabajaremos con lenguaje python


# control + s -> guardar cambios en archivo

numero = int(input("Ingrese un número entero: "))
print(numero)


# imprimiendo contenido

print("El valor ingresado es  " + str(numero)) # menos eficiente

print(f"El número ingresado fue {numero}")  # usando format string 'f'
autor="Gonzalo"
print("El numero ingresado fue : {} - autor: {}".format(numero, autor))

