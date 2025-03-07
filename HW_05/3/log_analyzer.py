# main.py
#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import re
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    # Парсинг рядка логу:
    regex = r"^(?P<timestamp>[\d-]+\s[\d:]+)\s(?P<level>\w+)\s(?P<message>.+)$"
    match = re.match(regex, line)
    if match:
        return match.groupdict()
    return None


def load_logs(file_path: str) -> list:
    # Завантаження логів з файлу:
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            parsed_line = parse_log_line(line.strip())
            if parsed_line:
                logs.append(parsed_line)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    # Фільтрація логів за рівнем:
    return list(filter(lambda log: log["level"].upper() == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    # Підрахунок записів за рівнем логування:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"].upper()] += 1
    return dict(counts)


def display_log_counts(counts: dict):
    # Вивід результатів у вигляді таблиці:
    print(f"{'Level':<10} | {'Count':<5}")
    print("-" * 20)
    for level, count in counts.items():
        print(f"{level:<10} | {count:<5}")


def main():
    if len(sys.argv) < 2:
        print(
            "Використання: python log_analyzer.py <шлях до файлу логів> [<рівень логування>] e.g [INFO-WARNING-ERROR-DEBUG]"
        )
        return

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)

    # Підрахунок записів за рівнем
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Фільтрація за рівнем логування, якщо вказано
    if len(sys.argv) == 3:
        level_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level_filter)
        print(f"\nЗаписи для рівня '{level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} {log['level']} {log['message']}")


if __name__ == "__main__":
    main()
