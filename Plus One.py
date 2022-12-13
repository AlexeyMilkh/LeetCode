"""Вам дано большое целое число, представленное в виде целочисленного массива цифр, где каждая цифра[i] — это i-я
цифра целого числа. Цифры упорядочены от наиболее значащего к наименее значащему в порядке слева направо. Большое
целое число не содержит ведущих нулей.

Увеличьте большое целое число на единицу и верните результирующий массив цифр."""
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    digit = int(''.join(map(str, digits))) + 1
    result = []
    for i in str(digit):
        result.append(int(i))
    return result


data1 = [1, 2, 3]
data2 = [4, 3, 2, 1]
data3 = [9]
print(plusOne(data1))