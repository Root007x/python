num_processes = int(input("Enter the number of processes: "))
num_resources = int(input("Enter the number of resources: "))

available = list(map(int, input("Enter the available resources: ").split()))

max_claim = []
for i in range(num_processes):
    max_claim.append(list(map(int, input(f"Enter the maximum resource claim for process P{i}: ").split())))

allocated = []
for i in range(num_processes):
    allocated.append(list(map(int, input(f"Enter the currently allocated resources for process P{i}: ").split())))

# Calculate the need matrix
need = []
for i in range(num_processes):
    need.append([max_claim[i][j] - allocated[i][j] for j in range(num_resources)])

# Check if a request for resources is safe
def is_safe_request(process_id, request):
    global available, allocated, need
    # Check if the request can be granted without exceeding the maximum claim
    if all([request[i] <= need[process_id][i] for i in range(num_resources)]):
        # Check if the request can be granted without causing a deadlock
        temp_available = available.copy()
        temp_allocated = [row.copy() for row in allocated]
        temp_need = [row.copy() for row in need]
        for i in range(num_resources):
            temp_available[i] -= request[i]
            temp_allocated[process_id][i] += request[i]
            temp_need[process_id][i] -= request[i]
        work = temp_available.copy()
        finish = [False] * num_processes
        while not all(finish):
            found = False
            for i in range(num_processes):
                if not finish[i] and all([temp_need[i][j] <= work[j] for j in range(num_resources)]):
                    work = [work[j] + temp_allocated[i][j] for j in range(num_resources)]
                    finish[i] = True
                    found = True
            if not found:
                return False
        return True
    else:
        return False

# Prompt the user for a resource request and check if it is safe
while True:
    process_id = int(input("Enter the process ID: "))
    request = list(map(int, input("Enter the resource request: ").split()))
    if is_safe_request(process_id, request):
        print("Request is safe and can be granted.")
        available = [available[i] - request[i] for i in range(num_resources)]
        allocated[process_id] = [allocated[process_id][i] + request[i] for i in range(num_resources)]
        need[process_id] = [need[process_id][i] - request[i] for i in range(num_resources)]
    else:
        print("Request is not safe and cannot be granted.")
    if input("Do you want to make another request? (y/n) ") == 'n':
        break
