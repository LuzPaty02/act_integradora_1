from KPM_p1 import buscar_codigo_malicioso_KMP
from Manacher_p2 import buscar_palindromo_manacher
from LCS_p3 import buscar_subsecuencia_lcs

def readfile(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    transmission1=readfile('transmission1.txt')
    transmission2=readfile('transmission2.txt')
    mcode1=readfile('mcode1.txt')
    mcode2=readfile('mcode2.txt')
    mcode3=readfile('mcode3.txt')

    print("Buscando código malicioso en la transmisión:")

