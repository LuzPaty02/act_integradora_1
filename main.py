from KPM_p1 import buscar_codigo_malicioso_KMP
# from Manacher_p2 import buscar_palindromo_manacher
# from LCS_p3 import buscar_subsecuencia_lcs

def readfile(filename):
    with open(filename, 'r') as file:
        data = file.read().replace("\n", "").replace(" ", "")  # Elimina saltos de línea y espacios
        return data

def main():
    #Lee los archivos de texto y los guarda en variables
    transmission1 = readfile('transmission1.txt')
    transmission2 = readfile('transmission2.txt')
    mcode1 = readfile('mcode1.txt')
    mcode2 = readfile('mcode2.txt')
    mcode3 = readfile('mcode3.txt')

    
    mcode_files = [mcode1, mcode2, mcode3]
    mcode_file_names= ['mcode1.txt', 'mcode2.txt', 'mcode3.txt'] # Para imprimir el nombre del archivo en caso de encontrar el código malicioso

    transmissions_files = [transmission1, transmission2]
    transmissions_files_names = ['transmission1.txt', 'transmission2.txt'] # Para imprimir el nombre del archivo en caso de encontrar el código malicioso

#PARTE 1
    print("Buscando código malicioso en la transmisión:")
    for mcode_index in range (len(mcode_files)):
        for transmission_index in range(len(transmissions_files)):
            found_malicious_code = buscar_codigo_malicioso_KMP(mcode_files[mcode_index], transmissions_files[transmission_index]) #guarda el resultado de la función:  la posición en el archivo de transmissiónX.txt donde inicia el código de mcodeY.txt

            if found_malicious_code is not None: #si sí encontró código malicioso
                #ejemplo de impresión: True 150 en transmission1.txt para mcode1.txt
                print(f"True {found_malicious_code} en {transmissions_files_names[transmission_index]} para {mcode_file_names[mcode_index]}")
            else:
                print(f"False en {transmissions_files_names[transmission_index]} para {mcode_file_names[mcode_index]}")

#PARTE 2

            
if __name__ == "__main__":
    main()