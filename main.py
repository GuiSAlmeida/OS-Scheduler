#################################################################
# Algorithms simulating OS scheduler process                    #
# Author: Guilherme Almeida                                     #
# Contact: https://www.guisalmeida.com                          #
#################################################################

import pandas as pd
from diagram import create_gantt
from algorithms import fifo, sjf, priority
import csv

filename = 'files/processos.csv'
procs = []

with open(filename, 'r') as csv_data:
    for line in csv.DictReader(csv_data):
        procs.append(dict(line))


def main(alg, procs):
    sorted_procs = alg(procs)

    df = pd.DataFrame(sorted_procs)
    df.to_csv(f'files/processos_{alg.__name__}.csv')

    create_gantt(sorted_procs, f'{alg.__name__}')


main(fifo, procs)
main(sjf, procs)
main(priority, procs)
