def get_input(n):
    process = []
    for i in range(n):
        arrival_time, burst_time, priority = map(int, input(
            f"Enter arrival,burst,priority for process[{i}] : ").split())
        process.append((i + 1, arrival_time, burst_time, priority))
    process.sort(key=lambda x: (x[1], x[3], x[2], x[0]))
    return process


def find_next_process(process, n, completed, current_time):
    max_priority = float('inf')
    max_arrival = float('inf')
    min_bt = float('inf')
    idx = -1

    for i in range(n):
        if not completed[i] and process[i][1] <= current_time:
            if process[i][3] < max_priority:
                max_priority = process[i][3]
                max_arrival = process[i][1]
                min_bt = process[i][2]
                idx = i
            elif process[i][3] == max_priority and process[i][1] < max_arrival:
                max_arrival = process[i][1]
                min_bt = process[i][2]
                idx = i
    return idx


def priority_preemtive():
    n = int(input("Enter number of process : "))
    proc = get_input(n)

    remaining_bt = [proc[i][2] for i in range(n)]
    completed = [False] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    current_time = 0

    while not all(completed):
        idx = find_next_process(proc, n, completed, current_time)
        if idx == -1:
            current_time += 1
        else:
            remaining_bt[idx] -= 1
            current_time += 1
            if remaining_bt[idx] == 0:
                completed[idx] = True
                complition_time = current_time
                turnaround_time[idx] = complition_time - proc[idx][1]
                waiting_time[idx] = turnaround_time[idx] - proc[idx][2]

    total_turnaround_time = sum(turnaround_time)
    total_waiting_time = sum(waiting_time)
    avg_turnaround_time = total_turnaround_time/n
    avg_waiting_time = total_waiting_time/n
    print(f"Avarage waiting Time : {avg_waiting_time : .2f}")
    print(f"Avarage Turnaround Time : {avg_turnaround_time : .2f}")


if __name__ == "__main__":
    priority_preemtive()
