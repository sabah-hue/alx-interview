#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys


status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
size = 0
count = 0
try:
    for line in sys.stdin:
        data = line.split()
        count += 1

        if len(data) >= 5 and data[-2].isdigit() and data[-1].isdigit():
            status_code = int(data[-2])
            if status_code in status_dict:
                status_dict[status_code] += 1

        if len(data) >= 6 and data[-1].isdigit():
            size += int(data[-1])

        if count % 10 == 0 or sys.stdin.closed:
            print(f"File size: {size}")
            for status_code in sorted(status_dict.keys()):
                if status_dict[status_code]:
                    print(f"{status_code}: {status_dict[status_code]}")

except KeyboardInterrupt:
    print(f"File size: {size}")
    for status_code in sorted(status_dict.keys()):
        if status_dict[status_code]:
            print(f"{status_code}: {status_dict[status_code]}")
    raise KeyboardInterrupt
