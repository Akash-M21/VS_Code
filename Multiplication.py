def multiply_numbers(numbers):
    """
    Multiplies a list of numbers, each between 1 and 999.
    
    Args:
    numbers (list of int): List of integers to multiply.
    
    Returns:
    int: The product of the numbers.
    """
    if not numbers:
        return 1  # Product of empty list is 1
    product = 1
    for num in numbers:
        if not (1 <= num <= 999):
            raise ValueError(f"Number {num} is not between 1 and 999")
        product *= num
    return product

# Example usage:
if __name__ == "__main__":
    nums = [2, 3, 4]  # Example list
    result = multiply_numbers(nums)
    print(f"The product is: {result}")