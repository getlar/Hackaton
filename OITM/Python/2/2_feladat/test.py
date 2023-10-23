def min_petrol_cost(prices, fuel_capacity, consumption_rate):
    n = len(prices)
    min_cost = [float('inf')] * (n + 1)
    min_cost[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            distance = (i - j) * 100
            fuel_needed = distance / 100 * consumption_rate
            cost = fuel_needed * prices[i - 1]

            if fuel_capacity >= fuel_needed:
                min_cost[i] = min(min_cost[i], min_cost[j] + cost)
            else:
                cost_to_fill = (fuel_needed - fuel_capacity) * prices[i - 1]
                min_cost[i] = min(min_cost[i], min_cost[j] + cost_to_fill)

    return min_cost[n]

prices = [150, 80, 200, 150, 100, 50, 150, 100, 200, 300, 235, 80, 167, 96, 83, 224, 186, 202, 127, 158, 105, 82, 135, 270, 158, 136, 156, 131, 123, 226, 238, 98, 94, 283, 275, 280, 97, 116, 223, 84, 288, 90, 267, 296, 144, 192, 297, 227, 232, 164, 239, 119, 279, 231, 188, 292, 178, 123, 93, 285, 197, 124, 218, 168, 197]
fuel_capacity = 40
consumption_rate = 10

result = min_petrol_cost(prices, fuel_capacity, consumption_rate)
print(f"The minimum cost of petrol for the trip is {result:.2f}")