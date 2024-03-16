"""
1. 最初の要素と次の要素を比較します。
2. もし次の要素の方が小さければ、それらの要素を交換します。
3. 次の要素とその次の要素を比較し、同様の交換を行います。
4. リストの終端まで到達するまで、この比較と交換のプロセスを繰り返します。
5. リストの終端に到達したら、最大の要素が確定し、次のパスに進みます。
6. パスを繰り返すごとに、確定した要素はリストの末尾に移動していきます。
"""

def bubble_sort(numbers: list) -> list[int]:
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

numbers = [5, 3, 8, 6, 1, 9, 2, 7]
print(bubble_sort(numbers))