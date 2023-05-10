num_processes = int(input("Enter the number of processes: "))
num_resources = int(input("Enter the number of resources: "))

available = list(map(int, input("Enter the available resources: ").split()))

max_claim = []
for i in range(num_processes):
    max_claim.append(list(
        map(int, input(f"Enter the maximum resource claim for process P{i}: ").split())))

allocated = []
for i in range(num_processes):
    allocated.append(list(map(int, input(
        f"Enter the currently allocated resources for process P{i}: ").split())))

# Calculate the need matrix
need = []
for i in range(num_processes):
    need.append([max_claim[i][j] - allocated[i][j]
                for j in range(num_resources)])

# Initialize the work and finish lists
work = available.copy()
finish = [False] * num_processes

# Find a safe sequence of processes
safe_sequence = []
while not all(finish):
    found = False
    for i in range(num_processes):
        if not finish[i] and all([need[i][j] <= work[j] for j in range(num_resources)]):
            work = [work[j] + allocated[i][j] for j in range(num_resources)]
            finish[i] = True
            safe_sequence.append(i)
            found = True
    if not found:
        print("System is not in safe state")
        break

print("Safe sequence of processes: ", end=" ")
for i in safe_sequence:
    print(f"P{i} ", end=" ")
