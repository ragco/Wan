class Job:
    def __init__(self, job_id, deadline, profit):
        """Constructor to initialize job details"""
        self.job_id = job_id  # Job identifier (e.g., 'J1', 'J2', etc.)
        self.deadline = deadline  # Deadline by which the job must be completed
        self.profit = profit  # Profit for completing the job

def job_scheduling(jobs):
    """Function to schedule jobs to maximize total profit"""
    
    # Step 1: Sort jobs in decreasing order of profit (Greedy approach)
    jobs.sort(key=lambda job: job.profit, reverse=True)

    # Step 2: Find the maximum deadline to determine the number of slots
    max_deadline = max(job.deadline for job in jobs)
    schedule = [-1] * max_deadline  # Initialize the schedule with -1 (empty slots)

    total_profit = 0  # To track the total profit earned by scheduling jobs
    job_sequence = []  # List to store the sequence of scheduled jobs

    # Step 3: Iterate over jobs to schedule them in the most optimal slots
    for job in jobs:
        # Step 4: Try to schedule the job in the latest available slot before its deadline
        for t in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if schedule[t] == -1:  # If the slot is empty
                schedule[t] = job.job_id  # Assign job to this slot
                total_profit += job.profit  # Add the job's profit to total profit
                job_sequence.append(job.job_id)  # Record the job in the job sequence
                break  # Once scheduled, stop checking other slots for this job

    # Output the result
    print("\nScheduled Jobs in order:", job_sequence)  # Display the sequence of scheduled jobs
    print("Total Profit:", total_profit)  # Display the total profit from scheduled jobs

# Main program to accept user input and call job scheduling function
n = int(input("Enter the number of jobs: "))  # Accept number of jobs from the user
jobs = []

# Step 1: Collect details for each job (job_id, deadline, and profit)
for i in range(n):
    print(f"\nEnter details for Job {i+1}:")
    job_id = input("Job ID: ")  # Accept job ID (e.g., 'J1')
    deadline = int(input("Deadline (positive integer): "))  # Accept the deadline
    profit = int(input("Profit: "))  # Accept the profit for the job
    jobs.append(Job(job_id, deadline, profit))  # Add the job object to the list

# Step 2: Call the function to schedule jobs and display the results
job_scheduling(jobs)


#Enter the number of jobs: 4
#Enter details for Job 1:
#Job ID: J1
#Deadline (positive integer): 4
#Profit: 20
#Enter details for Job 2:
#Job ID: J2
#Deadline (positive integer): 1
#Profit: 10
#Enter details for Job 3:
#Job ID: J3
#Deadline (positive integer): 1
#Profit: 40
#Enter details for Job 4:
#Job ID: J4
#Deadline (positive integer): 1
#Profit: 30