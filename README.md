
<h1 align="center">
  OS Scheduler Simulation
</h1>

Create a gantt chart to simulate the scaling processes of the operating system, using algorithms such as FIFO, SJB and priority. These algorithms order the processes and calculate the waiting time and the total time that each one obtained. Thus, it is possible to calculate the average waiting time that each process obtained and verify which algorithm obtained the best performance.

## 🏆 Challenge
- Write an application, to simulate process scheduling policies in **Priority, FIFO and Shortest Job First** algorithms.

- Simulate a process queue where who is using the CPU is
using until finishing the process (Single core).

## 🗃️ Data
|Process|Priority|Duration(ms)|Size(kb)|
|:---:|:---:|:---:|:---:|
|Process A|Priority 4|2|4|
|Process B|Priority 2|4|2|
|Process C|Priority 1|1|3|
|Process D|Priority 3|2|5|
|Process E|Priority 1|1|5|
|Process F|Priority 5|4|6|
|Process G|Priority 3|2|2|
|Process H|Priority 1|3|1|

## 📊 FIFO
<p align="center"><img src="./files/images/Screenshot from 2023-04-11 19-31-54.png" alt="FIFO-gantt-chart png" /></p>

## 📊 Shortest Job First
<p align="center"><img src="./files/images/Screenshot from 2023-04-11 19-32-10.png" alt="SJB-gantt-chart png" /></p>

## 📊 Priority
<p align="center"><img src="./files/images/Screenshot from 2023-04-11 19-32-22.png" alt="PRI-gantt-chart png" /></p>


<!-- ## 🛠️ Installation Steps

1. Clone the repository

```bash
git clone git@github.com:GuiSAlmeida/OS-Scheduler.git
```

2. Change the working directory

```bash
cd OS-Scheduler
```

3. Install libs

```bash
pip3 instal ...
```

4. Run main

```bash
python3 main.py
```

🌟 You are all set! -->


## 🛠️ Built with
- [Python](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/): for gantt chart.
- [Pandas](https://pandas.pydata.org/): for read and write csv files.
- [Numpy](https://numpy.org/): for arange data.

## 👨🏻‍💻 Author

[**Guilherme Almeida**](https://guisalmeida.com)

See also the list of [contributors](https://github.com/GuiSAlmeida/OS-Scheduler/contributors) who participated in this project.

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>
<p align="center">
Developed with ❤️ in Brazil 🇧🇷
</p>
