#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet == 101 or alphabet == 113:
        continue
    print('{:c}'.format(alphabet), end="")
