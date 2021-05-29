procs = [
    {'Processo': 'Processo A', 'Prioridade': '4', 'Tempo de Execução': '2', 'Tamanho': '4'},
    {'Processo': 'Processo B', 'Prioridade': '2', 'Tempo de Execução': '4', 'Tamanho': '2'},
    {'Processo': 'Processo C', 'Prioridade': '1', 'Tempo de Execução': '1', 'Tamanho': '3'},
    {'Processo': 'Processo D', 'Prioridade': '3', 'Tempo de Execução': '2', 'Tamanho': '5'},
    {'Processo': 'Processo E', 'Prioridade': '1', 'Tempo de Execução': '1', 'Tamanho': '5'},
    {'Processo': 'Processo F', 'Prioridade': '5', 'Tempo de Execução': '4', 'Tamanho': '6'},
    {'Processo': 'Processo G', 'Prioridade': '3', 'Tempo de Execução': '2', 'Tamanho': '2'},
    {'Processo': 'Processo H', 'Prioridade': '1', 'Tempo de Execução': '3', 'Tamanho': '1'}
]

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

def fifo(procs):
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


def sjf(procs):
    pass


def priority(procs):
    pass


print(fifo(procs))
