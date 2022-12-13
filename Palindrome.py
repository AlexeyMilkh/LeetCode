"""
Дано целое число x. Вернуть True, если x является палиндромом, в противном случае вернуть False
"""


def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]
