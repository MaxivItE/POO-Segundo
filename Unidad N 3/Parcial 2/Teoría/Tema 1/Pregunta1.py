
def agregar(l, d):
    assert (type(d) == int)
    l.append(int(d))

def mostrar(l, p):
    assert (type(p) == int)
    print("En la posición {} está el elemento {}" .format(p, l[p]))

if __name__ == '__main__':
    lista=[]
    agregar(lista,10)
    agregar(lista,8)
    agregar(lista,9)
    #agregar(lista,'0')
    #mostrar(lista,1)
    #agregar(lista,9.3)
    #mostrar(lista,'0')
    #agregar(lista,5)
    #agregar(lista,'R')

'''
Seleccione una o más de una:
☐ a. Con la instrucción agregar(lista,'0') arroja un AssertionError y luegose agrega a la lista el valor 0.
☑ b. La instruccion mostrar(lista,1) muestra por pantalla "En la posición 1 está el elemento 8".
☐ c. Con la instrucción agregar(lista,9.3) el 9.3 se trunca a 9 y se agrega este valor a la lista.
☐ d. Considerando el programa dado, la instrucción mostrar(lista,'0') arrojaría un excepción TypeError.
☑ e. Considerando el programa dado, la instrucción mostrar(lista,5) arrojaría una excepción.
☑ f. La instrucción agregar(lista,'R') arroja un AssertionError.
'''



