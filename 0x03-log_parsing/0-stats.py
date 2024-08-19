#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys


status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
size = 0
count = 0
c = 0
try:
    for line in sys.stdin:
        data = line.split()
        data_invert = data[::-1]

        if len(data_invert) > 2:
            count += 1

            if count <= 10:
                size += int(data_invert[0])
                c = data_invert[1]

                if c in status_dict.keys():
                    status_dict[c] += 1

            if count == 10:
                print(f"File size: {size}")
                for k, v in sorted(status_dict.items()):
                    if v != 0:
                        print(f"{k}: {v}")
                count = 0

finally:
    print(f"File size: {size}")
    for k, v in sorted(status_dict.items()):
        if v != 0:
            print(f"{k}: {v}")
