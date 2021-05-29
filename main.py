from diagram import create_gantt
import csv

filename = 'lista_processos.csv'
procs = []

with open(filename, 'r') as csv_data:
    for line in csv.DictReader(csv_data):
        procs.append(dict(line))

print(procs)


# procs = [
#     {
#         "Processo": 'Processo A',
#         "Prioridade": 4,
#         "Tempo de Execução": 2,
#         "Tamanho": 4,
#         "Tempo de Espera": 0,
#         "Tempo Total": 5,
#     },
# ]

# create_gantt(procs)
