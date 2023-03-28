def get_process(n):
    process = []
    for i in range(n):
        arrival_time = int(input(f"Enter Arrival Time {i+1} : "))
        burst_time = int(input(f"Enter Burst Timme {i+1} : "))
        process.append((i+1,arrival_time,burst_time))

    for j in range(n):
        print(process[j])


    

if __name__ == "__main__":
    n = 5
    get_process(n)
