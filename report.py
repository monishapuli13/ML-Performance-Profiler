os.makedirs("reports", exist_ok=True)
import csv
import os


def save_report(elapsed, throughput, memory_mb):
    file_exists = os.path.exists("reports/results.csv")

    with open(
        "reports/results.csv",
        "a",
        newline=""
    ) as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "elapsed_time",
                "throughput",
                "memory_mb"
            ])

        writer.writerow([
            elapsed,
            throughput,
            memory_mb
        ])