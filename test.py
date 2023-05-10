# This program implements a round robin scheduling algorithm considering all corner cases.

# Define a process class.
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.state = "ready"
        self.waiting_time = 0
        self.turnaround_time = 0

# Define a function to sort the processes by arrival time.
def sort_processes(processes):
    processes.sort(key=lambda process: process.arrival_time)

# Define a function to schedule the processes.
def schedule_processes(processes, time_quantum):
    # Initialize the ready queue.
    ready_queue = []

    # Initialize the current time.
    current_time = 0

    # Loop until all processes have been scheduled.
    while len(processes) > 0:
        # Get the process with the earliest arrival time.
        process = processes.pop(0)

        # If the process is not ready, add it to the ready queue.
        if process.state == "ready":
            ready_queue.append(process)
            continue

        # Start the process.
        process.state = "running"

        # Update the current time.
        current_time += time_quantum

        # Update the process's burst time.
        process.burst_time -= time_quantum

        # If the process is not finished, add it back to the ready queue.
        if process.burst_time > 0:
            ready_queue.append(process)

        # Update the process's waiting time and turnaround time.
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = current_time - process.arrival_time + process.burst_time

        # If the process has finished, remove it from the ready queue and print its stats.
        if process.burst_time == 0:
            processes.remove(process)
            print("Process ID | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
            print(process.pid, process.arrival_time, process.burst_time, process.waiting_time, process.turnaround_time)

    # If there are still processes in the ready queue, schedule them again.
    while len(ready_queue) > 0:
        process = ready_queue.pop(0)
        process.state = "running"
        process.burst_time = process.burst_time
        current_time = process.arrival_time
        # Check to see if the process is in the list before trying to remove it.
        if process in processes:
            processes.remove(process)
            schedule_processes([process], time_quantum)

# Define a function to get user input.
def get_user_input():
    # Get the number of processes.
    n = int(input("Enter the number of processes: "))

    # Get the arrival times of the processes.
    arrival_times = []
    for i in range(n):
        arrival_time = int(input("Enter the arrival time of process {}: ".format(i + 1)))
        arrival_times.append(arrival_time)

    # Get the burst times of the processes.
    burst_times = []
    for i in range(n):
        burst_time = int(input("Enter the burst time of process {}: ".format(i + 1)))
        burst_times.append(burst_time)

    # Create a list of processes.
    processes = []
    for i in range(n):
        processes.append(Process(i + 1, arrival_times[i], burst_times[i]))

    return processes

# Get user input.
processes = get_user_input()