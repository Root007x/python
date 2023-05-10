def get_input(n):
    process = []
    for i in range(n):
        arrival, burst, priority = map(int, input(
            f"Enter arrival,burst,pririty for process {i} : ").split())
        process.append((i + 1, arrival, burst, priority))
    process.sort(key=lambda x: (x[1], x[3], x[2]))
    return process


def find_next_process(process, n, current_time, completed):
    max_priority = float('inf')
    min_bt = float('inf')
    idx = -1
    for i in range(n):
        if not completed[i] and process[i][1] <= current_time:
            if process[i][3] < max_priority:
                max_priority = process[i][3]
                min_bt = process[i][2]
                idx = i
            elif process[i][3] == max_priority and process[i][2] < min_bt:
                min_bt = process[i][2]
                idx = i
    return idx


def priority_nonPreemtive():
    n = int(input("Enter number of process : "))
    proc = get_input(n)

    completed = [False] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    current_time = 0

    while not all(completed):
        idx = find_next_process(proc, n, current_time, completed)
        if idx == -1:
            current_time += 1
        else:
            completed[idx] = True
            complition_time = current_time + proc[idx][2]
            turnaround_time[idx] = complition_time - proc[idx][1]
            waiting_time[idx] = turnaround_time[idx] - proc[idx][2]
            current_time = complition_time

    total_turnaround_time = sum(turnaround_time)
    total_waiting_time = sum(waiting_time)
    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n

    print(f"Avarage Waiting Time : {avg_waiting_time : .2f}")
    print(f"Avarage Turnaround Time : {avg_turnaround_time : .2f}")


if __name__ == "__main__":
    priority_nonPreemtive()
