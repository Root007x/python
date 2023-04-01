def get_processes(n):
    processes = []
    for i in range(n):
        arrival_time, burst_time = map(int, input(f"Enter arrival time and burst time for process {i+1}: ").split())
        if arrival_time < 0 or burst_time <= 0:
            print("Invalid input. Arrival time must be non-negative and burst time must be positive.")
            return None
        processes.append((i+1, arrival_time, burst_time))
    processes.sort(key=lambda x: x[1])
    return processes


def round_robin(q):
    n = int(input("Enter the number of processes: "))
    processes = None
    while processes is None:
        processes = get_processes(n)

    current_time = 0
    completed = [False] * n
    remaining_time = [process[2] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    queue = []

    while not all(completed):
        for i in range(n):
            if not completed[i] and processes[i][1] <= current_time:
                queue.append(i)

        if not queue:
            current_time += 1
            continue

        idx = queue.pop(0)
        if remaining_time[idx] > q:
            current_time += q
            remaining_time[idx] -= q
            queue.append(idx)
        else:
            current_time += remaining_time[idx]
            completion_time = current_time
            waiting_time[idx] = completion_time - processes[idx][1] - processes[idx][2]
            turnaround_time[idx] = completion_time - processes[idx][1]
            remaining_time[idx] = 0
            completed[idx] = True
            print(f"Complition Time : {completion_time}")

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")


if __name__ == '__main__':
    q = int(input("Enter the time quantum: "))
    round_robin(q)

