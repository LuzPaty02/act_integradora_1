def crear_LPS(mcode, m):
    LPS = [0] * m  # Inicializar el array LPS
    length = 0  # Longitud del prefijo más largo que también es sufijo
    i = 1

    # Construir el array LPS
    while i < m:
        if mcode[i] == mcode[length]: 
            length += 1
            LPS[i] = length
            i += 1
        else:
            if length != 0:
                length = LPS[length - 1]
            else:
                LPS[i] = 0
                i += 1
    return LPS



def buscar_codigo_malicioso_KMP(mcode, transmission):

    m = len(mcode)
    n = len(transmission)

    LPS = crear_LPS(mcode, m)

    i = 0  # índice para la transmisión
    j = 0  # índice para el patrón (mcode)

    while i < n:  # Recorrer la transmisión
        if mcode[j] == transmission[i]:  # Si los caracteres coinciden
            i += 1
            j += 1

        if j == m:  # Si se recorrió todo el patrón
            return i - j

        elif i < n and mcode[j] != transmission[i]:  # Si hay discordancia
            if j != 0:
                j = LPS[j - 1]  # Saltar usando el array LPS
            else:
                i += 1  # Si no hay coincidencias parciales, avanzar en el texto

    return None  # Si no se encuentra el patrón


""" 
KMP algotithm

se basa en recordar hasta qué punto han coincidido los caracteres entre el patrón y el texto, 
y cuando hay una discordancia, vuelve a la última posición donde hubo coincidencia y aprovecha esa información 
para saltar partes del patrón que ya no es necesario comparar de nuevo.
Esto lo hace utilizando el array LPS (longest prefix suffix)
Prefijo: Subcadena que va desde el inicio del patrón hasta antes del final.
Sufijo: Subcadena que empieza después del primer carácter y termina en el final del patrón.


¿Cómo funciona el LPS? Almacena la longitud del prefijo más largo que también es un sufijo de una subcadena del patrón.
Ejemplo:
patrón = "ABABC"
LPS = [0, 0, 1, 2, 0]
A -> No hay prefijo ni sufijo posibles porque solo hay un carácter.
AB -> Prefijos: "" (cadena vacía) y "A". Sufijos: "B" y "" (cadena vacía). Ningún prefijo coincide con un sufijo.
ABA -> Prefijos: "", "A" y "AB". Sufijos: "A", "BA" y "ABA". El prefijo "A" coincide con el sufijo "A". LPS[2] = 1.
ABAB -> Prefijos: "", "A", "AB" y "ABA". Sufijos: "B", "AB", "BAB" y "ABAB". El prefijo "AB" coincide con el sufijo "AB". LPS[3] = 2.
ABABC -> Prefijos: "", "A", "AB", "ABA" y "ABAB". Sufijos: "C", "BC", "ABC", "BABC" y "ABABC". Ningún prefijo coincide con un sufijo.

Cuando hay una discordancia, en lugar de retroceder en el texto, el algoritmo "salta" a una posición del patrón 
que sigue siendo compatible con las coincidencias anteriores, utilizando la información del **LPS** para continuar
la búsqueda eficientemente.
"""

