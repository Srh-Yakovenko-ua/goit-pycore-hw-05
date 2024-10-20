from typing import Callable
import re

# Regular expression pattern for identifying real numbers, separated by spaces
number_pattern = r"\b[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?\b"


# Function that generates numbers
def number_generator(text: str):
    # Find all numbers in the text using the regular expression
    numbers = re.findall(number_pattern, text)

    # Yield numbers as floats
    for num in numbers:
        try:
            yield float(num)
        except ValueError:
            continue


# Function to calculate the total sum of numbers
def sum_profit(text: str, generator_func: Callable):
    # Call the function that returns the generator
    number_list = list(generator_func(text))

    # If there are no numbers, return 0
    if not number_list:
        return 0

    # Return the sum of all numbers
    return sum(number_list)


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

if __name__ == "__main__":

    total_income = sum_profit(text, number_generator)
    print(f"Total income: {total_income}")
