from typing import List


def calculate_adjusted_value(original_value: float, multiplier: float = 1.15) -> float:
    """
    Calculate the adjusted value by applying a multiplier.
    
    Args:
        original_value: The original numeric value
        multiplier: The multiplier to apply (default: 1.15 for 15% increase)
    
    Returns:
        The adjusted value
    """
    return original_value * multiplier


def format_value_output(value: float) -> str:
    """
    Format a numeric value as a human-readable string.
    
    Args:
        value: The numeric value to format
    
    Returns:
        Formatted string representation
    """
    return f"Total: {value:.2f}"


def log_results(results: List[float], log_file: str = "log.txt") -> None:
    """
    Write results to a log file.
    
    Args:
        results: List of values to log
        log_file: Path to the log file (default: "log.txt")
    """
    with open(log_file, "a") as f:
        f.write(str(results) + "\n")


def display_results(results: List[float]) -> None:
    """
    Display results to the console.
    
    Args:
        results: List of values to display
    """
    for result in results:
        formatted_output = format_value_output(result)
        print(formatted_output)


def process_data(data: List[float], multiplier: float = 1.15) -> List[float]:
    """
    Process data by applying a multiplier, displaying, and logging results.
    
    This is the main orchestrator function that coordinates the workflow.
    
    Args:
        data: List of numeric values to process
        multiplier: The multiplier to apply (default: 1.15)
    
    Returns:
        List of adjusted values
    """
    adjusted_values = [calculate_adjusted_value(value, multiplier) for value in data]
    display_results(adjusted_values)
    log_results(adjusted_values)
    return adjusted_values
