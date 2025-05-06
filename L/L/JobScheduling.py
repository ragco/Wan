# Take input from the user
n = int(input("Enter the number of jobs: "))

profit = []
jobs = []
deadline = []

for i in range(n):
    job = input(f"Enter job name for job {i + 1}: ")
    jobs.append(job)
    p = int(input(f"Enter profit for {job}: "))
    profit.append(p)
    d = int(input(f"Enter deadline for {job}: "))
    deadline.append(d)

profitNJobs = list(zip(profit, jobs, deadline))
profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

slot = [0] * (max(deadline) + 1)  # Create slots based on the maximum deadline
profit = 0
ans = ['null'] * (max(deadline) + 1)

for i in range(len(jobs)):
    job = profitNJobs[i]
    # Check if slot is occupied
    for j in range(job[2], 0, -1):
        if slot[j] == 0:
            ans[j] = job[1]
            profit += job[0]
            slot[j] = 1
            break

# Print the scheduled jobs and total profit
print("Jobs scheduled:", [job for job in ans if job != 'null'])
print("Total profit:", profit)