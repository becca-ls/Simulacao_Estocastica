import random
import os
import datetime
import csv

csvFile = 'C:/Users/rls/Documents/estocástica/Atividade_1/executionTime_float.csv'

mode = 'a'  # read mode
lista = []
tamanho = 1000000

if not os.path.exists(csvFile):
    mode = 'w'  # mode write if the file does not exist


def write(content: list[str], file):
    writer = csv.writer(file)
    if mode == 'w':
        writer.writerow([
            'start', 'end', 'delta'
        ])
    writer.writerow(content)

for _ in range(tamanho):
    elemento = round(random.uniform(1.0, 10000.0), 3)
    lista.append(elemento)

start = datetime.datetime.now()

# Algorithm
soma = 0
for elemento in lista:
    soma += elemento

# Pos-processing

end = datetime.datetime.now()
delta = end - start

file = open(csvFile, mode)

write([str(data) for data in [start, end, delta]], file)
file.close()
