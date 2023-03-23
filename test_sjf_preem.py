def get_processes(n):
    processes = []
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        if arrival_time < 0 or burst_time <= 0:
            print("Invalid input. Arrival time must be non-negative and burst time must be positive.")
            return None
        processes.append((i+1, arrival_time, burst_time, burst_time)) # added remaining time to track remaining burst time
    processes.sort(key=lambda x: (x[1], x[2]))
    return processes

# pick the process id which has smallest remaining burst time
def find_next_process(processes, n, completed, current_time):
    min_bt = float('inf')
    min_idx = -1
    for i in range(n):
        if not completed[i] and processes[i][1] <= current_time and processes[i][3] < min_bt:
            min_bt = processes[i][3]
            min_idx = i
    return min_idx


def sjf_preemptive():
    n = int(input("Enter the number of processes: "))
    processes = None
    while processes is None:
        processes = get_processes(n)

    current_time = 0
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    while not all(completed):
        idx = find_next_process(processes, n, completed, current_time)
        if idx == -1:
            current_time += 1
        else:
            processes[idx] = (processes[idx][0], processes[idx][1], processes[idx][2], processes[idx][3]-1) # execute process for one time unit
            current_time += 1
            if processes[idx][3] == 0: # process has completed execution
                completed[idx] = True
                completion_time = current_time
                turnaround_time[idx] = completion_time - processes[idx][1]
                waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
    
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        completion = str(turnaround_time[i] + processes[i][1]) if completed[i] else 'NA'  # calculate completion time for each process
        turnaround = str(turnaround_time[i]) if completed[i] else 'NA'
        waiting = str(waiting_time[i]) if completed[i] else 'NA'
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion}\t\t{turnaround}\t\t\t{waiting}")

    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")

if __name__ == '__main__':
    sjf_preemptive()