import sys, string

def guardar_string_matriz(string: string) -> list[list[string]]:
    n = len(string)
    ret_matrix = [[0] * n for letras in string]
    for i in range(n):
        for j in range(n):
            if(i==j):
                ret_matrix[i][j] = True
            else:
                ret_matrix[i][j] = False
    return ret_matrix

if __name__ == "__main__":
    ret_matrix = guardar_string_matriz("holasoyhomero")
    for i in range(len(ret_matrix)):
        print(f"{ret_matrix[i]}")
