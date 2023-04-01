def get_processes(n):
    processes = []
    for i in range(n):
        arrival_time, burst_time, priority = map(int, input(f"Enter arrival time, burst time, and priority for process {i+1}: ").split())
        if arrival_time < 0 or burst_time <= 0 or priority < 1:
            print("Invalid input. Arrival time must be non-negative, burst time must be positive, and priority must be greater than or equal to 1.")
            return None
        processes.append((i+1, arrival_time, burst_time, priority))
    processes.sort(key=lambda x: (x[1], x[3], x[2], x[0]))
    return processes

def find_next_process(processes, n, completed, current_time):
    max_priority = float('inf')
    min_bt = float('inf')
    min_arrival = float('inf')
    min_idx = -1
    for i in range(n):
        if not completed[i] and processes[i][1] <= current_time:
            if processes[i][3] < max_priority:
                max_priority = processes[i][3]
                min_bt = processes[i][2]
                min_arrival = processes[i][1]
                min_idx = i
            elif processes[i][3] == max_priority and processes[i][1] < min_arrival:
                min_arrival = processes[i][1]
                min_bt = processes[i][2]
                min_idx = i

    return min_idx


def priority_preemptive():
    n = int(input("Enter the number of processes: "))
    processes = None
    while processes is None:
        processes = get_processes(n)

    current_time = 0
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_bt = [processes[i][2] for i in range(n)]
    
    while not all(completed):
        idx = find_next_process(processes, n, completed, current_time)
        if idx == -1:
            current_time += 1
        else:
            remaining_bt[idx] -= 1
            current_time += 1
            if remaining_bt[idx] == 0:
                completed[idx] = True
                completion_time = current_time
                turnaround_time[idx] = completion_time - processes[idx][1]
                waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
                print(f"Complition Time : {completion_time}")
            
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")

if __name__ == '__main__':
    priority_preemptive()


