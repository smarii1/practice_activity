def vacation(money, days, cost):
    n = len(cost)

    min_cost_of_vacation = float('inf')
    for i in range(n - days + 1):
        current_cost = sum(cost[i:i + days])
        if current_cost < min_cost_of_vacation:
            min_cost_of_vacation = current_cost

    if min_cost_of_vacation <= money:
        return f"money: {min_cost_of_vacation}"
    else:
        max_days_in_vacation = 0
        for d in range(1, days):
            for i in range(n - d + 1):
                current_cost = sum(cost[i:i + d])
                if current_cost <= money:
                    if d > max_days_in_vacation:
                        max_days_in_vacation = d
        return f"days: {max_days_in_vacation}"

print(vacation(20, 2, [10]))
print(vacation(10, 3, [3, 8, 6]))
print(vacation(30, 3, [15, 18, 10]))
print(vacation(30, 1, [25, 10, 30]))
print(vacation(50, 1, [35, 30, 20]))
print(vacation(80, 3, [40, 55, 75]))
