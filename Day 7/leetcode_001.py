def two_sum_brute(nums, target):
    # O(n²) — slow but simple — two nested loops
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_optimal(nums, target):
    # O(n) — fast — hash map solution
    seen = {}   # stores {number: index}

    for i, num in enumerate(nums):
        complement = target - num   # what number do I need?

        if complement in seen:      # have I seen it before?
            return [seen[complement], i]

        seen[num] = i   # remember this number and its index

    return []

# Test both
print(two_sum_brute([2, 7, 11, 15], 9))    # [0, 1]
print(two_sum_optimal([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_optimal([3, 2, 4], 6))       # [1, 2]
print(two_sum_optimal([3, 3], 6))          # [0, 1]