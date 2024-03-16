"""
適当に並び替えを行うアルゴリズム
猿でもできるソートとも呼ばれる
"""


import random

def in_order(numbers: list) -> bool:
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

def bogo_sort(numbers: list) -> list[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

print(bogo_sort([1, 5, 6, 7, 2, 4]))