"""Для заданной строки s, состоящей из слов и пробелов, вернуть длину последнего слова в строке.
Слово – это максимальная подстрока, состоящая только из не пробельных символов."""


def lengthOfLastWord(s: str) -> int:
    return len(s.rstrip().split(sep=' ')[-1])


data = "Hello World"
print(lengthOfLastWord(data))
