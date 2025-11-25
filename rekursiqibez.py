def sum_list_iterative(nums: list[int]) -> int:
    total = 0
    for v in nums:
        total += v
    return total

def sum_list_recursive(nums: list[int]) -> int:
    if not nums:
        return 0
    return nums[0] + sum_list_recursive(nums[1:])

def reverse_string_iterative(s: str) -> str:
    return s[::-1]

def reverse_string_recursive(s: str) -> str:
    if s == "":
        return ""
    return reverse_string_recursive(s[1:]) + s[0]

def fib_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

if __name__ == "__main__":
    print("=== Sum of list ===")
    print(f"Iterative: {sum_list_iterative([1, 2, 3, 4, 5])}")
    print(f"Recursive: {sum_list_recursive([1, 2, 3, 4, 5])}")
    
    print("\n=== Reverse string ===")
    print(f"Iterative: {reverse_string_iterative('Hello')}")
    print(f"Recursive: {reverse_string_recursive('Hello')}")
    
    print("\n=== Fibonacci ===")
    print(f"Iterative (10): {fib_iterative(10)}")
    print(f"Recursive (10): {fib_recursive(10)}")
