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
            proc["Waiting time"] = wait
            proc['Total time'] = int(proc['Runtime']) + int(proc['Waiting time'])
            continue

        wait += int(procs[index - 1]['Runtime'])

        proc['Waiting time'] = wait
        proc['Total time'] = int(proc['Runtime']) + int(proc['Waiting time'])

    return procs


def fifo(procs):
    return set_wait_time(procs)


def sjf(procs):
    sjf_procs = sorted(procs, key=lambda proc: proc['Size'])
    return set_wait_time(sjf_procs)


def priority(procs):
    pri_procs = sorted(procs, key=lambda proc: proc['Priority'])  # to asc set thirty param (reverse=True)
    return set_wait_time(pri_procs)
