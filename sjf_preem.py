def sort(proc, current_time):
    n = len(proc)
    for i in range(n):
        for j in range(n-i-1):
            if proc[j][3] > proc[j+1][3] or (proc[j][3] == proc[j+1][3] and proc[j][1] < proc[j+1][1]):
                proc[j], proc[j+1] = proc[j+1], proc[j]

def findNextProcess(proc, current_time):
    n = len(proc)
    min_burst = float('inf')
    next_proc = -1
    for i in range(n):
        if proc[i][1] <= current_time and proc[i][3] < min_burst and proc[i][3] > 0:
            min_burst = proc[i][3]
            next_proc = i
    return next_proc

def findAvgTime(proc):
    n = len(proc)
    current_time = 0
    total_wt = 0
    total_tat = 0
    completed = 0
    # Initialize remaining burst time to the burst time for all processes
    for i in range(n):
        proc[i][3] = proc[i][2] # remaining_time
    while completed != n:
        next_proc = findNextProcess(proc, current_time)
        if next_proc == -1:
            current_time += 1
            continue
        if proc[next_proc][3] == proc[next_proc][2]:
            proc[next_proc][4] = current_time # start_time
        proc[next_proc][3] -= 1 # remaining_time
        current_time += 1
        if proc[next_proc][3] == 0:
            completed += 1
            wt = current_time - proc[next_proc][1] - proc[next_proc][2] # arrival_time, burst_time
            tat = current_time - proc[next_proc][1] # arrival_time
            total_wt += wt
            total_tat += tat
            proc[next_proc][5] = current_time # end_time
            print(f"Process {proc[next_proc][0]}\tArrival Time: {proc[next_proc][1]}\tBurst Time: {proc[next_proc][2]}\tStart Time: {proc[next_proc][4]}\tEnd Time: {proc[next_proc][5]}\tWaiting Time: {wt}\tTurnaround Time: {tat}")
        else:
            sort(proc, current_time) # sort the processes by remaining burst time and arrival time (if burst times are equal)
    # Calculate average waiting time and turnaround time
    avg_wt = float(total_wt) / n
    avg_tat = float(total_tat) / n
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    proc = []
    for i in range(n):
        arrival_time, burst_time = map(int, input(f"Enter arrival time and burst time for process {i+1}: ").split())
        proc.append([i+1, arrival_time, burst_time, 0, 0, 0]) # pid, arrival_time, burst_time, remaining_time, start_time, end_time
    sort(proc, 0) # sort the processes by arrival time
    findAvgTime(proc)




