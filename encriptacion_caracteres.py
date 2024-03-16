cadena_string = "la vida es bella"
array_caracteres = list(cadena_string)

""" 
l =  $
a = 7
v = %
i = #
d = &
e = R
s = Q
b = Y
  = N
"""


encriptation = ""
for position, letter in enumerate(array_caracteres):
    t = ""
    if (letter == 'l'):
        encriptation = encriptation + "$"
        t = '$'
    elif letter == 'a':
        encriptation = encriptation + "7"
        t = "7"
    elif letter == ' ':
        encriptation = encriptation + "N"
        t = "N"
    elif letter == 'v':
        encriptation = encriptation + "%"
        t = "%"
    elif letter == 'i':
        encriptation = encriptation + "#"
        t = "#"
    elif letter == 'd':
        encriptation = encriptation + "&"
        t = "&"
    elif letter == 'e':
        encriptation = encriptation + "R"
        t = "R"
    elif letter == 's':
        encriptation = encriptation + "Q"
        t = "Q"
    elif letter == 'b':
        encriptation = encriptation + "Y"
        t = "Y"

    print("token:", t, "posicion:", position)

list_desencriptacion = list(encriptation)
desencriptacion = ""
for letter in list_desencriptacion:
    if letter == '$':
        desencriptacion = desencriptacion + "l"
    elif letter == '7':
        desencriptacion = desencriptacion + "a"
    elif letter == 'N':
        desencriptacion = desencriptacion + " "
    elif letter == '%':
        desencriptacion = desencriptacion + "v"
    elif letter == '#':
        desencriptacion = desencriptacion + "i"
    elif letter == '&':
        desencriptacion = desencriptacion + "d"
    elif letter == 'R':
        desencriptacion = desencriptacion + "e"
    elif letter == 'Q':
        desencriptacion = desencriptacion + "s"
    elif letter == 'Y':
        desencriptacion = desencriptacion + "b"

print("Encriptacion = ", encriptation)
print("Desencriptacion = ", desencriptacion)
print("Cantidad de caracteres = ", len(array_caracteres))
