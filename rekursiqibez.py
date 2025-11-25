def sum_list_iterative(nums: list[int]) -> int:
    total = 0  
    for v in nums:
        total += v 
    return total

def sum_list_recursive(nums: list[int]) -> int:
    if not nums:
        return 0  # при празен списък
    return nums[0] + sum_list_recursive(nums[1:])  # рекурсивно добавяне на първия елемент

def reverse_string_iterative(s: str) -> str:
    return s[::-1]

def reverse_string_recursive(s: str) -> str:
    if s == "":
        return ""  # при празен низ
    # рекурсивно обръщане на остатъка и добавяне на първия символ в края
    return reverse_string_recursive(s[1:]) + s[0]

def fib_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")  # валидация на входа
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")  # валидация на входа
    if n == 0:
        return 0  # базов случай
    if n == 1:
        return 1  # базов случай
    return fib_recursive(n - 1) + fib_recursive(n - 2)  # рекурсивна стъпка

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