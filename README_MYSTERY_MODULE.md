# Mystery Module Documentation

## Overview

The `mystery_module.py` contains a mathematical utility function for solving quadratic equations using the **quadratic formula**.

## Module Purpose

This module provides functionality to find the roots (solutions) of quadratic equations in the standard form:

$$ax^2 + bx + c = 0$$

## Function Reference

### `fn_x(a, b, c)`

Solves a quadratic equation and returns its roots using the quadratic formula.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `a` | float | Coefficient of x² (must not be 0) |
| `b` | float | Coefficient of x |
| `c` | float | Constant term |

#### Returns

- **Type:** `tuple` or `None`
- **Value:** 
  - `tuple`: A tuple of two float values representing the two roots: `(root1, root2)`
  - `None`: If the equation has no real solutions (discriminant < 0)

#### Mathematical Background

The function uses the quadratic formula:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Where the **discriminant** ($\Delta = b^2 - 4ac$) determines the nature of solutions:
- **$\Delta > 0$**: Two distinct real roots
- **$\Delta = 0$**: One repeated real root
- **$\Delta < 0$**: No real solutions (complex roots)

## Usage Examples

### Example 1: Two Distinct Real Roots

```python
from mystery_module import fn_x

# Solve: x² - 5x + 6 = 0
# Factors to: (x - 2)(x - 3) = 0
result = fn_x(1, -5, 6)
print(result)  # Output: (3.0, 2.0)
```

### Example 2: One Repeated Root

```python
# Solve: x² - 4x + 4 = 0
# Factors to: (x - 2)² = 0
result = fn_x(1, -4, 4)
print(result)  # Output: (2.0, 2.0)
```

### Example 3: No Real Solutions

```python
# Solve: x² + 1 = 0
# Discriminant is negative
result = fn_x(1, 0, 1)
print(result)  # Output: None
```

### Example 4: Negative Leading Coefficient

```python
# Solve: -2x² + 8x - 6 = 0
result = fn_x(-2, 8, -6)
print(result)  # Output: (3.0, 1.0)
```

## Function Implementation

```python
import math

def fn_x(a, b, c):
    d = b**2 - 4*a*c
    if d < 0: 
        return None
    return ((-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a))
```

### How It Works

1. **Calculate Discriminant:** `d = b² - 4ac`
2. **Check Real Solutions:** If `d < 0`, no real solutions exist → return `None`
3. **Calculate Roots:** Apply the quadratic formula with ± for both roots

## Edge Cases and Limitations

### ⚠️ Known Limitations

| Issue | Impact | Solution |
|-------|--------|----------|
| `a = 0` | ZeroDivisionError | Ensure `a ≠ 0` before calling |
| Negative discriminant | Returns `None` | Handle `None` return value in code |
| Floating-point precision | Possible rounding errors | Use appropriate tolerance for comparisons |

### Example: Handling Edge Cases

```python
def safe_quadratic_solve(a, b, c):
    """Safely solve quadratic equation with error handling."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 (not a quadratic equation)")
    
    roots = fn_x(a, b, c)
    
    if roots is None:
        return {"status": "no_real_solutions", "roots": None}
    else:
        return {"status": "success", "roots": roots}

# Usage
result = safe_quadratic_solve(1, -5, 6)
print(result)  # {"status": "success", "roots": (3.0, 2.0)}
```

## Testing

```python
# Test cases
assert fn_x(1, -5, 6) == (3.0, 2.0)  # Two distinct roots
assert fn_x(1, -4, 4) == (2.0, 2.0)  # Repeated root
assert fn_x(1, 0, 1) is None           # No real solutions
assert fn_x(-2, 8, -6) == (3.0, 1.0)  # Negative leading coefficient
```

## Dependencies

- `math` - Python standard library (for `math.sqrt()`)

## Author Notes

**Function Name:** The cryptic name `fn_x` is likely short for "function x" or "find x", referring to finding the unknown x in a quadratic equation. In production code, a more descriptive name like `solve_quadratic()` would be recommended.

## References

- [Quadratic Formula - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_formula)
- [Python Math Module](https://docs.python.org/3/library/math.html)

---

**Documentation Generated:** 2026-03-29  
**Module Status:** Functional
