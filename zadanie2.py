#!/usr/bin/env python3

for i in range(2000,3000):
    if i % 7 == 0 and i != i % 5:
        print(i, end=", ")