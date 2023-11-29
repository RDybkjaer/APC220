#!/usr/bin/env python3
import sys

import subprocess


def main():
    recursive()


def recursive():
    print("Recursing")
    while True:
        subprocess.call("/home/dyb/Documents/APC220/recursive.py", shell=False)
        limit = sys.getrecursionlimit()
        try:
            print(limit)
        except:
            print(limit)
            sys.setrecursionlimit(limit + 1)
            recursive()


if __name__ == "__main__":
    try:
        main()
    except:
        recursive()
