edad=int(input ("¿Qué edad tiene? "))

if edad >=18:
    print(f"Usted es mayor de edad {edad}")
elif edad <18 and edad >=0:
    print(f"Usted es menor de edad {edad}")
else:
    print(f"Edad incorrecta {edad}")