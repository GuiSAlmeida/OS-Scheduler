#################################################################
# Algorithms simulating OS scheduler process                    #
# Author: Guilherme Almeida                                     #
# Contact: https://www.guisalmeida.com                          #
#################################################################

import matplotlib.pyplot as plt
import numpy as np
from random import random


def add_proc(gantt, procs, proc):
    t_wait = int(proc["Waiting time"])
    duration = int(proc["Runtime"])

    assert t_wait >= 0, f"Error in process {proc}, start time cannot be negative."
    assert duration > 0, f"Error in process {proc}, duration must be greater than zero."

    r = random()
    g = random()
    b = random()
    color = (r, g, b)

    index = procs.index(proc)

    gantt.broken_barh(
        [(t_wait, duration)],
        (index, 1),
        facecolor=color,
        label=f'{proc["Process"]}'
    )

    gantt.text(
        x=(t_wait + duration / 2),
        y=(index + 0.5),
        s=f'{duration}ms\n{proc["Size"]}kb\nP{proc["Priority"]}',
        va="center",
        ha="center",
        color="white",
        weight='bold'
    )


def create_gantt(procs, name):
    procs = procs[::-1]
    lenght = len(procs)
    t_total = procs[0]["Total time"]
    ylabels = [proc["Process"] for proc in procs]
    fig, gantt = plt.subplots(figsize=(16, 9))

    fig.suptitle('Process execution map on a single core CPU', fontsize=28)
    gantt.set_title(f'Algorithm {name}', fontsize=18)

    total = 0
    for proc in procs:
        total += proc['Total time']
    average = total / len(procs)

    gantt.set_xlabel(f'Average waiting time per process: {average}ms', fontsize=18)
    gantt.set_ylabel('Processs', fontsize=18)

    gantt.set_xlim(0, t_total)
    gantt.set_ylim(0, lenght)

    gantt.set_xticks(range(0, t_total + 1), minor=False)
    gantt.grid(True, axis='x', which='both')

    gantt.set_yticks(range(1, lenght), minor=True)
    gantt.grid(True, axis='y', which='minor')

    gantt.set_yticks(np.arange(0.5, lenght + 0.5, 1))
    gantt.set_yticklabels(ylabels)

    for proc in procs:
        add_proc(gantt, procs, proc)

    plt.legend()
    plt.show()
