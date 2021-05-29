from diagram import create_gantt
from algorithms import fifo
import csv

filename = 'lista_processos.csv'
procs = []

with open(filename, 'r') as csv_data:
    for line in csv.DictReader(csv_data):
        procs.append(dict(line))


fifo_procs = fifo(procs)

create_gantt(fifo_procs)
