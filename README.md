# Number Analyzer

A Python-based interactive command-line application that performs various mathematical operations and checks on numbers.

## Overview

Number Analyzer is a beginner-friendly tool that helps users explore fundamental mathematical properties of numbers. The application provides an intuitive menu-driven interface for performing three core operations: checking if numbers are even or odd, determining if numbers are prime, and calculating square roots with customizable precision.

## Features

### 1. Even/Odd Checker
- Determines whether a given number is even or odd
- Accepts both integers and floating-point numbers
- Real-time validation and result display

### 2. Prime Number Checker
- Validates if a number is prime
- Uses optimized algorithm checking divisibility up to the square root
- Handles edge cases (numbers less than 2)

### 3. Square Root Calculator
- Calculates the exact square root of any positive number
- Provides multiple output formats:
  - Exact value (full precision)
  - Rounded to specified decimal places (default: 3)
  - Rounded to nearest integer
- Customizable decimal precision

## Technical Architecture

### Core Components

- **`main_launcher.py`**: Entry point and menu system
- **`logic.py`**: Mathematical operation implementations
- **`validator.py`**: Input validation and user interaction handling

### Class Structure

#### Logic Class
Handles all mathematical computations:
- `is_even_or_odd()`: Modulo-based even/odd detection
- `is_prime()`: Prime number validation using trial division
- `square_root()`: Square root calculation with multiple precision options

#### Validate Class
Manages user input and validation flows:
- `parse_input()`: Generic input parser with error handling
- `validate_even_odd()`: Even/odd checker workflow
- `validate_prime()`: Prime checker workflow
- `validate_square_root()`: Square root calculator workflow

## Dependencies

- **Python 3.10+** (uses modern type hints with union operator `|`)
- **math** (standard library)
- **haashi_pkg.utility.utils**: Custom utility package for screen management

## Usage

### Running the Application

```bash
python main_launcher.py
```

### Menu Navigation

Upon launch, users are presented with four options:

1. Check if a number is even or odd
2. Check if a number is prime
3. Calculate the square root of a number
4. Exit

Enter the corresponding number (1-4) to select an operation.

### Input Format

- Enter any positive number when prompted
- Type `q` to return to the main menu from any operation
- Invalid inputs are caught and users are re-prompted

### Example Workflow

```
Choose an operation:
1. Check if a number is even or odd.
2. Check if a number is prime.
3. Calculate the square root of a number.
4. Exit.

Enter your choice (1-4): 1

Enter a integer to check if it is even or odd (or 'q' to return to main-menu)
>>> 42

42.0 is an even number.
```

## Error Handling

The application includes robust error handling:
- **Invalid input types**: Non-numeric inputs are rejected with clear error messages
- **Negative numbers**: Rejected as invalid (since even/odd and prime checks expect positive numbers)
- **Keyboard interrupts**: Gracefully exits the program
- **Out-of-range menu choices**: Users are notified and re-prompted

## Design Patterns

- **Separation of Concerns**: Logic separated from validation and UI
- **Type Safety**: Type hints used throughout for better code documentation
- **User-Friendly**: Auto-clearing prompts and timed screen management
- **Continuous Operation**: Each feature runs in a loop until user chooses to exit

## Future Enhancements

Potential areas for expansion:
- Add factorial calculation
- Include GCD/LCM operations
- Support for complex numbers
- Export results to file
- Batch processing mode


## Author

Haashiraaa

## Contributing

Contributions, issues, and feature requests are welcome!
