import csv
import os
from datetime import datetime

def log_scan(url, result):

    file_exists = os.path.isfile("scan_logs.csv")

    with open("scan_logs.csv", "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "url",
                "result"
            ])

        writer.writerow([
            datetime.now(),
            url,
            result
        ])
        print("Logged:", url, result)