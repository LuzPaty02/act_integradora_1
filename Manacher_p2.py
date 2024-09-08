def preprocesar_cadena(cadena):
    return "#" + "#".join(cadena) + "#"

def buscar_palindromo_manacher(transmission):
    transmission_string = preprocesar_cadena(transmission.strip())  # Preprocesar la cadena
    n = len(transmission_string)

    P = [0] * n  # Array para guardar el radio de los palíndromos
    center = 0
    right = 0

    for i in range(n):
        mirror = 2 * center - i  # Calcular el índice espejo de i con respecto al centro

        if i < right:
            P[i] = min(right - i, P[mirror])  # Limitar el radio según la simetría

        # Expandir el palíndromo centrado en i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and transmission_string[i + P[i] + 1] == transmission_string[i - P[i] - 1]:
            P[i] += 1

        # Actualizar el centro y el borde derecho si el palíndromo expandido es más grande
        if i + P[i] > right:
            center = i
            right = i + P[i]

    # Depurar el array P y el centro detectado
    print(f"Array P: {P}")
    print(f"Center index: {center}, Right limit: {right}")

    # Encontrar el índice del palíndromo más largo
    max_length = max(P)  # Longitud máxima del palíndromo
    center_index = P.index(max_length)  # El índice central del palíndromo más largo

    # Convertir de la cadena preprocesada a la original
    start = (center_index - max_length) // 2  # Convertir la posición a la cadena original
    end = start + max_length - 1  # Calcular el fin del palíndromo

    # Depurar el palíndromo más largo encontrado
    palindromo = transmission[start:end+1]
    print(f"Palíndromo más largo encontrado: '{palindromo}' en posiciones {start+1} a {end+1} en la cadena original")

    return start + 1, end + 1  # Retornar las posiciones 1-based


""" 
Manacher algorithm
- eficiente para encontrar el palíndromo más largo dentro de una cadena
- Objetivo del algoritmo: Encontrar la subcadena más larga dentro de una cadena dada que sea un palíndromo.
¿Cómo funciona?
- Inserta un carácter especial, como #, entre cada carácter del string para tratar los palíndromos de longitud par e impar 
de la misma manera.
- Esto asegura que todos los palíndromos sean de longitud impar.

Proceso de propagación del radio:
P[]: Almacena el radio del palíndromo más largo en cada posición.
Si tienes una cadena original "abac", la preprocesamos como "#a#b#a#c#". El array P[] podría verse así:

#a#b#a#c#
P = [0, 1, 0, 3, 0, 1, 0, 0, 0]
Esto significa:
En la posición 1 (donde está a), hay un palíndromo de radio 1: "a".
En la posición 3 (donde está b), hay un palíndromo de radio 3: "aba".
En otras posiciones, el radio es menor o no hay palíndromos más largos.

center y right: Mantienen el centro y el borde derecho del palíndromo más largo encontrado hasta el momento.

El algoritmo trata de expandir los palíndromos 
Si estamos dentro del palíndromo actual (es decir, i < right), podemos usar la simetría de los palíndromos:
El palíndromo centrado en la posición i tiene un "espejo" en la posición mirror, donde 

mirror = 2 * center - i.


Si el radio en la posición mirror es más pequeño que la distancia entre i y right, entonces sabemos que el palíndromo en i
será como mínimo tan largo como el palíndromo en mirror.

Si el carácter a la izquierda de i - P[i] es igual al carácter a la derecha de i + P[i], extendemos el palíndromo incrementando P[i].
Actualización de center y right

Resultado: Una vez que se ha calculado el array P[], el palíndromo más largo tiene el mayor valor en P[], 
y las posiciones del palíndromo más largo en la cadena original se calculan a partir de esa posición.
Ejemplo:
cadena = "abac"
cadena_preprocesada = "#a#b#a#c#"
P = [0, 1, 0, 3, 0, 1, 0, 0, 0]
center = 3
right = 6 
El palíndromo más largo es "aba".
Las posiciones en la cadena original son 1 y 3 (donde la primera "a" está en la posición 1 y la última "a" está en la posición 3).
"""