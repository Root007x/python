class RoundRobin:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            arrival_time, burst_time = map(int, input(
                f"Enter Arrival Time and Burst Time for process {i + 1}: ").split())

            temporary.extend(
                [i + 1, arrival_time, burst_time, 0, burst_time])
            process_data.append(temporary)

        time_slice = int(input("Enter Time Slice: "))

        RoundRobin.schedulingProcess(self, process_data, time_slice)

    def schedulingProcess(self, process_data, time_slice):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])

        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1

                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i]
                                    [1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []

                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert(
                                    (len(ready_queue) - 1), ready_queue.pop(k))

                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i]
                                [1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break

            if len(ready_queue) != 0:

                if ready_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                    ready_queue.pop(0)

                elif ready_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]

                if normal_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice

                elif normal_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)

        RoundRobin.calculation(self, process_data)

    def calculation(self, process_data):
        total_turnaround_time = 0
        total_waiting_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)

        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)

        average_waiting_time = total_waiting_time / len(process_data)
        average_turnaround_time = total_turnaround_time / len(process_data)
        print(f"Avarage Trunaround Time : {average_turnaround_time: .2f}")
        print(f"Avarage Waiting Time : {average_waiting_time: .2f}")


if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    rr = RoundRobin()
    rr.processData(no_of_processes)
