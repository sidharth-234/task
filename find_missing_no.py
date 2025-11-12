def find_missing_number(nums):
    n = len(nums) + 1  
    total = n * (n + 1) // 2
    return total - sum(nums)



numbers = list(map(int, input("Enter numbers separated by space: ").split()))

missing = find_missing_number(numbers)
print(f"The missing number is {missing}")
