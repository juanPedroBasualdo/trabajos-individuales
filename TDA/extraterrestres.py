import sys

# MEMORIZACION Y RECONSTRUCCIÓN DE SOLUCION

def palindromo_mas_largo(s: str) -> str:
    """
    Toma un string cuyas palabras estan todas pegadas:
    - Guarda en una matriz true si entre [i] y [j] hay un palindromo.
    - Guarda el inicio y la longitud maxima del último palindromo encontrado.
    - Devuelve el string de parametro pero recortado en la seccion palindromica mas larga.
    """
    n = len(s)
    opt = [[False] * n for _ in range(n)]
    inicio, maximo = 0, 1

    for i in range(n):
        opt[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            opt[i][i+1] = True
            inicio, maximo = i, 2

    for long in range(3, n+1):
        for i in range(n - long + 1):
            j = i + long - 1
            if s[i] == s[j] and opt[i+1][j-1]:
                opt[i][j] = True
                if long > maximo:
                    inicio, maximo = i, long

    return s[inicio:inicio+maximo]

# MAIN

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print(f"Uso: {sys.argv[0]} <numero>")
        sys.exit(1)

    mensaje = sys.argv[1]
    palabra_importante = palindromo_mas_largo(mensaje)
    print(f"{palabra_importante}")
   
