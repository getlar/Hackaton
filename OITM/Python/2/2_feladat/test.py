capacity = 40
mileage = 10
costs = [150, 80, 200, 150, 100, 50, 150, 100, 200, 300, 235, 80, 167, 96, 83, 224, 186, 202, 127, 158, 105, 82, 135, 270, 158, 136, 156, 131, 123, 226, 238, 98, 94, 283, 275, 280, 97, 116, 223, 84, 288, 90, 267, 296, 144, 192, 297, 227, 232, 164, 239, 119, 279, 231, 188, 292, 178, 123, 93, 285, 197, 124, 218, 168, 197]

# Utility functions
def cost(i):
    return costs[i - 1]

def dist(i, j):
    return (j-i)*100

def minTank(i, j, x):
    return max(0, x - dist(i, j) / mileage)

def maxTank(i, j, y):
    return min(capacity, y + dist(i, j) / mileage)

def findMinCost(i, j):
    minIndex = i
    minCost = cost(minIndex)
    for k in range(i + 1, j - 1):
        print(cost(k), minCost)
        if cost(k) < minCost:
            minIndex = k
            minCost = cost(k)
    return minIndex

# Get optimal filling amounts
def getOptimalHelper(i, j, x, y):
    if j == i + 1:
        petrolSpent = 100 / mileage
        toBuy = y - (x - petrolSpent)
        if toBuy < 0 or x + toBuy > capacity:
            return None
        return [[toBuy], cost(i) * toBuy]

    k = findMinCost(i, j)
    if k == i:
        targetTank = maxTank(i, j, y)
        toBuy = targetTank - x
        thisCost = cost(i) * toBuy
        rightOpt = getOptimalHelper(i + 1, j, targetTank - 100 / mileage, y)
        if rightOpt is None:
            return None
        rightAmounts, rightCost = rightOpt
        return [[toBuy] + rightAmounts, thisCost + rightCost]

    tankOnArrivalAtK = minTank(i, k, x)
    leftOpt = getOptimalHelper(i, k, x, tankOnArrivalAtK)
    if leftOpt is None:
        return None
    rightOpt = getOptimalHelper(k, j, tankOnArrivalAtK, y)
    if rightOpt is None:
        return None
    leftAmounts, leftCost = leftOpt
    rightAmounts, rightCost = rightOpt
    return [leftAmounts + rightAmounts, leftCost + rightCost]

# Get the overall optimal solution
def getOptimal(i, j, x):
    return getOptimalHelper(i, j, x, minTank(i, j, x))

# Calculate the overall optimal solution
overallOptimal = getOptimal(1, len(costs) + 1, capacity - 100 / mileage)

if overallOptimal is None:
    print('It is not possible to reach the destination.')
else:
    amounts, totalCost = overallOptimal
    print("Total cost = Rs.", totalCost)
    print("Amounts of petrol to be bought:")
    print(amounts)