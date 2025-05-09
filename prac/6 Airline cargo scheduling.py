# pip install pulp

from pulp import LpProblem, LpVariable, lpSum, LpMaximize, LpStatus

# Take input from users for parameters
max_flights_per_day = int(input("Enter the maximum number of flights per day: "))
max_cargo_capacity_per_flight = int(input("Enter the maximum cargo capacity per flight: "))
demand = [int(input(f"Enter the demand for day {i+1}: ")) for i in range(5)]  # Assuming 5 days
cargo_capacity = [int(input(f"Enter the cargo capacity for flight {i+1}: ")) for i in range(5)]  # Assuming 5 flights

# Create LP problem
prob = LpProblem("Airline Scheduling", LpMaximize)

# Decision variables
x = [LpVariable(f"Flight_{i}", lowBound=0, cat="Integer") for i in range(len(demand))]

# Objective function
prob += lpSum(x), "Total flights scheduled"

# Constraints
for i in range(len(demand)):
    prob += x[i] <= max_flights_per_day, f"Max flights constraint for day {i+1}"
    prob += x[i] * max_cargo_capacity_per_flight >= demand[i], f"Cargo capacity constraint for day {i+1}"

# Solve the problem
prob.solve()

# Print the results
print("Status:", LpStatus[prob.status])
print("Optimal Schedule:")
for i, v in enumerate(prob.variables()):
    print(f"Day {i+1}: {int(v.varValue)} flights")
