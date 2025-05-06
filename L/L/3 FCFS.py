def fcfs(jobs):
    # Sort jobs based on their arrival times
    jobs.sort(key=lambda x: x[0])

    schedule = []

    current_time = 0
    for arrival_time, burst_time in jobs:
        # Determine the start time of the job (maximum of current time and arrival time)
        start_time = max(current_time, arrival_time)
        # Determine the end time of the job
        end_time = start_time + burst_time
        # Append job details to the schedule
        schedule.append((start_time, end_time))
        # Update current time to the end time of the current job
        current_time = end_time

    return schedule

# Example usage:
jobs = [(0, 6), (1, 8), (2, 7), (3, 3), (4, 5)]  # (arrival_time, burst_time)
job_schedule = fcfs(jobs)
for start_time, end_time in job_schedule:
    print(f"Start Time = {start_time}, End Time = {end_time}")