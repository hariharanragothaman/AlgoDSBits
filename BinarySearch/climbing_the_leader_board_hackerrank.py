#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

def reverse_bisect(scores, value):
    low, high = 0, len(scores)
    while low < high:
        mid = (low + high) // 2
        if value > scores[mid]:
            high = mid
        else:
            low = mid + 1
    return low

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    print("The scores are:", scores)
    print("Alices score are:", alice)
    # Initial logic to store the ranking
    hash_map, rank = {}, 1
    for i in range(len(scores)):
        if scores[i] not in hash_map:
            hash_map[scores[i]] = rank
            rank += 1
    print("The hash_map is:", hash_map)


    # Applying binary search recipe
    output = []
    for i in range(len(alice)):
        idx = reverse_bisect(scores, alice[i])
        print("The index is:", idx)

        if idx == 0:
            output.append(1)
            continue

        prev_value = scores[idx-1]
        prev_rank = hash_map[prev_value]
        if prev_value == alice[i]:
            output.append(prev_rank)
        else:
            output.append(prev_rank + 1)
        print("*************")

    return output


if __name__ == '__main__':
    scores = list(map(int, input().rstrip().split()))
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print("The result is:", result)
