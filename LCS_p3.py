def buscar_subsecuencia_lcs(transmission1, transmission2):
    n = len(transmission1)
    m = len(transmission2)
    
    L = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0
    end_pos = 0
    
#Se crea una matriz de n+1 x m+1, donde n y m son las longitudes de las dos transmisiones.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if transmission1[i - 1] == transmission2[j - 1]: #Si los caracteres son iguales
                L[i][j] = L[i - 1][j - 1] + 1 
                if L[i][j] > max_len: 
                    max_len = L[i][j]
                    end_pos = i #Guarda la posición final del substring común más largo
            else:
                L[i][j] = 0



    start_pos = end_pos - max_len + 1
    return start_pos, end_pos

