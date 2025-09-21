import sys
 
# FUNCIONES AUXILIARES 

def int_a_array(num: int) -> list[int]:
    """
    Toma un entero y lo convierte en un array cuyos valores son cada digito del entero
    """
    return [int(digit) for digit in str(num)]

def rango_array(array: list[int]) -> (int,int):
    """
    Toma un array y devuelve su minimo y su maximo
    """
    max = 0
    for i in range(0, len(array)):
        if max == 0:
            max = array[i]
            min = array[i]
        if array[i] > max:
            max = array[i]
        if array[i] < min:
            min = array[i]
    return (min,max)
        
def counting_sort_array(array: list[int]) -> list[int]:
    """
    Auxiliar de counting sort que devuelve el array de conteo de datos
    """
    (min,max) = rango_array(array)
    aux_array = [0] * max

    for i in range(0, len(array)):
        aux_array[(array[i] - 1)] += 1
    
    return aux_array

def reconstruir_counting_sort(array: list[int], array_count: list[int]) -> list[int]:
    """
    Auxiliar de counting sort que reconstruye el array original
    a partir de el array de conteo
    """
    ret_array = [0] * len(array)
    siguiente_cantidad = 0
    cantidad = 0
    for j in range(1, len(array_count) + 1):
        siguiente_cantidad += (array_count[j - 1])
        for k in range(cantidad, siguiente_cantidad):
            ret_array[k] = j
        cantidad += (array_count[j - 1])

    return ret_array

def counting_sort(array: list[int]) -> list[int]:
    """
    Counting sort ordena un array de enteros respecto a la cantidad de veces que aparece
    un entero dentro del array, puesto en un array de conteo cuyos indices representan
    un valor dentro del array
    """
    aux_array = counting_sort_array(array)
    return reconstruir_counting_sort(array, aux_array)
    
        
def reconstruir_int_de_array(array: list[int]) -> int:
    """
    Toma un array de enteros y reconstruye su valor original dentro de los valores del array
    """
    num = int(''.join(str(digit) for digit in array))
    return num

# FUNCIONES DE ESCENARIO

def verificar_centro(array: list[int]) -> int:
    """
    Toma un array ordenado y se fija si existe un valor que no tiene par:
    - Si no existe tal valor, retorna 0
    - Si existe retorna el valor
    - Si existe más de un valor que no tiene par retorna -1
    """
    centro = 0
    i = 0
    
    while i < len(array):
        if i == len(array) - 1:
            if centro != 0:
                return -1
            return array[i]
        if array[i] != array[i + 1]:
            if centro != 0:
                return -1
            centro = array[i]
            i += 1
        else:
            i += 2
    
    return centro

def espejar_escenario_sin_centro(array: list[int]) -> list[int]:
    """
    Toma un array con pares de valores ordenados y 
    los coloca espejados desde el medio hacia afuera.
    """
    ret_array = [0] * len(array)
    n = len(array)
    mitad = n // 2

    i = 0
    k = 0
    while k < n - 1:
        actual = array[i] 

        j = (mitad - 1) - (i // 2)
        k = mitad + (i // 2)

        ret_array[j] = actual
        ret_array[k] = actual

        i += 2  

    return ret_array

def quitar_centro(array: list[int], centro: int) -> list[int]:
    """
    Coloca un 0 en el primer lugar en donde aparece el valor centro del escenario
    """
    n = len(array)
    for i in range(0, n):
        if (array[i] == centro):
            array[i] = 0
            return array

def espejar_escenario_y_centro(array: list[int], centro: int) -> list[int]:
    """
    Toma un array de pares de valores ordenados y un centro, coloca
    el centro de un array en el medio de un array de retorno,
    luego coloca cada dato de los pares del array de manera espejada.
    """
    ret_array = [0] * len(array)
    n = len(array)
    mitad = n // 2
    array = quitar_centro(array, centro)

    ret_array[mitad] = centro
    i = 0
    k = 0
    while k < n - 1:
        actual = array[i]
        if(actual == 0):
            i += 1
        else:
            j = (mitad - 1) - (i // 2)
            k = mitad + ((i // 2) + 1)

            ret_array[j] = actual
            ret_array[k] = actual

            i += 2
    return ret_array

def formar_escenario(array: list[int]) -> list[int]:
    """
    Forma el escenario:
    - Si no se puede formar retorna array = [-1]
    - Si se puede, retorna un array de retorno dependiendo el caso.
    """
    aux_array = counting_sort(array)
    centro = verificar_centro(aux_array)
    if(centro == 0):
        ret_array = espejar_escenario_sin_centro(aux_array)
    elif(centro > 0):
        ret_array = espejar_escenario_y_centro(aux_array, centro)
    else:
        ret_array = [-1]
    return ret_array

# MAIN

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print(f"Uso: {sys.argv[0]} <numero>")
        sys.exit(1)
    
    sectores = int(sys.argv[1])
    array_sectores = int_a_array(sectores)
    array_escenario = formar_escenario(array_sectores)
    escenario = reconstruir_int_de_array(array_escenario)
    
    if(escenario == -1):
        print(f"no es posible formar el escenario")
    else:
        print(f"{escenario}")

