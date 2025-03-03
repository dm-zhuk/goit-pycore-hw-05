from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    for part in text.split():
        try:
            yield float(part)
        except ValueError:
            continue


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))  # Generator for numbers sum up


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: ${total_income}")  # Загальний дохід: $1351.46
