#1
def reloj(numero):
    lista =[]
    for i in range(numero, -1, -1):
        lista.append(i)
        return lista
print(reloj(5))

#2
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

print(imprimir_y_devolver([1,2]))

#3
def primero_mas_longitud(lista):
    return lista[0] + len(lista)

print(primero_mas_longitud(1,2,3,4,5))

#4
def Valores_mayores_que_el_segundo(lista):
    for valor in lista:
        if valor > lista[1]:
            print(valor)

Valores_mayores_que_el_segundo(5,2,3,2,1,4)

#5

