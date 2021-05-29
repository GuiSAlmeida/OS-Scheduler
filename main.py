#################################################################
# Algorithms simulating OS scheduler process                    #
# Author: Guilherme Almeida                                     #
# Contact: https://www.guisalmeida.com                          #
#################################################################

from diagram import create_gantt
from algorithms import fifo, sjf, priority
import csv

filename = 'lista_processos.csv'
procs = []

with open(filename, 'r') as csv_data:
    for line in csv.DictReader(csv_data):
        procs.append(dict(line))

fifo_procs = fifo(procs)
create_gantt(fifo_procs, 'FIFO - first in first out')

# sjf_procs = sjf(procs)
# create_gantt(sjf_procs, 'SJF - shortest job first')

# pri_procs = priority(procs)
# create_gantt(pri_procs, 'Priority')
