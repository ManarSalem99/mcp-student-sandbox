def average_ratios(numbers):
    """
    Calculate the average of ratios (100 / each number).
    
    Args:
        numbers: List of numeric values
    
    Returns:
        Average of the ratios
    
    Raises:
        ValueError: If the list contains zero or is empty
        TypeError: If any element is not numeric
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if any(num == 0 for num in numbers):
        raise ValueError("Input list cannot contain zero (division by zero)")
    
    try:
        total = sum(100 / num for num in numbers)
        return total / len(numbers)
    except TypeError:
        raise TypeError("All elements in the list must be numeric")


# Test cases
if __name__ == "__main__":
    # This will now raise an informative error instead of crashing
    try:
        print(average_ratios([10, 5, 0]))
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example with valid input
    print(f"Valid input result: {average_ratios([10, 5, 2])}")
