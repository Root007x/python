def get_processes(n):
    processes = []
    for i in range(n):
        arrival_time, burst_time, priority = map(int, input(f"Enter arrival time, burst time, and priority for process {i+1}: ").split())
        if arrival_time < 0 or burst_time <= 0 or priority < 1:
            print("Invalid input. Arrival time must be non-negative, burst time must be positive, and priority must be greater than or equal to 1.")
            return None
        processes.append((i+1, arrival_time, burst_time, priority))
    processes.sort(key=lambda x: (x[1], x[3], x[2]))
    return processes



def find_next_process(processes, n, completed, current_time):
    max_priority = float('inf')
    min_bt = float('inf')
    min_idx = -1
    for i in range(n):
        if not completed[i] and processes[i][1] <= current_time:
            if processes[i][3] < max_priority:
                max_priority = processes[i][3]
                min_bt = processes[i][2]
                min_idx = i
            elif processes[i][3] == max_priority and processes[i][2] < min_bt:
                min_bt = processes[i][2]
                min_idx = i
    return min_idx


def priority_non_preemptive():
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
            completed[idx] = True
            completion_time = current_time + processes[idx][2]
            waiting_time[idx] = completion_time - processes[idx][1] - processes[idx][2]
            turnaround_time[idx] = completion_time - processes[idx][1]
            current_time = completion_time

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print("Process\tArrival Time\tBurst Time\tPriority\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        completion = str(turnaround_time[i] + processes[i][1]) if completed[i] else 'NA'
        turnaround = str(turnaround_time[i]) if completed[i] else 'NA'
        waiting = str(waiting_time[i]) if completed[i] else 'NA'
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{processes[i][3]}\t\t{completion}\t\t{turnaround}\t\t\t{waiting}")

    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")


if __name__ == '__main__':
    priority_non_preemptive()


