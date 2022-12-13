"""Римские цифры представлены семью различными символами: I, V, X, L, C, D и M. Римские цифры обычно пишутся слева
направо от большего к меньшему. Однако цифра четыре не "IIII". Вместо этого цифра четыре пишется как "IV". Так как
единица предшествует пятерке, мы вычитаем ее и получаем четыре. Тот же принцип применим к числу девять,
которое пишется как IX. Есть шесть случаев, когда используется вычитание:
    I можно поставить перед V (5) и X (10), чтобы получились 4 и 9.
    X можно поставить перед L (50) и C (100), чтобы получилось 40 и 90.
    C можно поставить перед D (500) и M (1000), чтобы получились 400 и 900.
Дана римская цифра, преобразовать ее в целое число."""


def romanToInt(s: str) -> int:
    roman_table = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}  # отображаем таблицу в словарь

    #  Решение с помощью реверсивного цикла

    num = 0  # Инициализация переменной для добавления значений, перебирая строку
    last = "I"  # Инициализация переменной для добавления последнего символа

    for numeral in s[::-1]:  # Обходим реверсивным циклом от меньшего к большему
        if roman_table[numeral] < roman_table[last]:  # Если значение меньше, чем последнее, которое мы видели
            num -= roman_table[numeral]  # Вычитаем из суммы
        else:
            num += roman_table[numeral]  # Иначе складываем в сумму
        last = numeral  # Устанавливаем следующее значение

    return num