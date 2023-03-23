def fcfs(proc, n):
    # Sort processes by their arrival time
    proc = sorted(proc, key=lambda p: p[1])

    # Initialize variables
    timer = 0
    total_wait_time = 0
    total_turnaround_time = 0

    # Calculate completion time, wait time, and turnaround time
    for i in range(n):
        # Check if the process has arrived
        if timer < proc[i][1]:
            timer = proc[i][1]

        # Calculate completion time, wait time, and turnaround time
        completion_time = timer + proc[i][2]
        wait_time = timer - proc[i][1]
        turnaround_time = completion_time - proc[i][1]

        # Update total wait time and total turnaround time
        total_wait_time += wait_time
        total_turnaround_time += turnaround_time

        # Update timer
        timer = completion_time

        # Print process information
        print(f"{proc[i][0]}\t {proc[i][1]}\t\t {proc[i][2]}\t\t {completion_time}\t\t\t {turnaround_time}\t\t\t {wait_time}")

    # Calculate average wait time and average turnaround time
    average_wait_time = total_wait_time / n
    average_turnaround_time = total_turnaround_time / n

    # Print average wait time and average turnaround time
    print(f"Average Wait Time: {average_wait_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    proc = []
    for i in range(n):
        print(f"Process {i+1}:")
        arrival_time = int(input("Enter the arrival time: "))
        burst_time = int(input("Enter the burst time: "))
        proc.append((i+1, arrival_time, burst_time))
    fcfs(proc, n)
