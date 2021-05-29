#################################################################
# Algorithms simulating OS scheduler process                    #
# Author: Guilherme Almeida                                     #
# Contact: https://www.guisalmeida.com                          #
#################################################################


def set_wait_time(procs):
    wait = 0
    for proc in procs:
        index = procs.index(proc)

        if index == 0:
            proc["Tempo de Espera"] = wait
            proc['Tempo Total'] = int(proc['Tempo de Execução']) + int(proc['Tempo de Espera'])
            continue

        wait += int(procs[index - 1]['Tempo de Execução'])

        proc['Tempo de Espera'] = wait
        proc['Tempo Total'] = int(proc['Tempo de Execução']) + int(proc['Tempo de Espera'])

    return procs


def fifo(procs):
    return set_wait_time(procs)


def sjf(procs):
    sjf_procs = sorted(procs, key=lambda proc: proc['Tamanho'])
    return set_wait_time(sjf_procs)


def priority(procs):
    pri_procs = sorted(procs, key=lambda proc: proc['Prioridade'], reverse=True)
    return set_wait_time(pri_procs)
