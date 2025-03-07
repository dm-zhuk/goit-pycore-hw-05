from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    for part in text.split():
        try:
            yield float(part)
        except ValueError:
            continue


def extract_numbers(text: str, func: Callable) -> list:
    return list(func(text))  # Convert the generator to a list

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

    numbers = extract_numbers(text, generator_numbers)
    sum_profit = sum(numbers)
    
    print(f"Дохід: {numbers}")  # [1000.01, 27.45, 324.0]
    print(f"Загальний дохід: {sum_profit} доларів.")  # .. $1351.46