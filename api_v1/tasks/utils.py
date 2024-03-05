async def fib_sum(stop_value: int, prev_value: int, next_value: int) -> int:
    """
    Поиск суммы элементов последовательности фибоначи, если элемент является четным
    :param stop_value: максимально значение элемента последовательности на котором функция заканчивает работу
    :param prev_value: первое значение последовательности
    :param next_value: второе значение последовательности
    :return: сумма всех четных элементов последовательности
    """
    total_sum = sum([value for value in (prev_value, next_value) if value % 2 == 0])

    while next_value < stop_value:
        prev_value, next_value = next_value, prev_value + next_value
        if next_value % 2 == 0:
            total_sum += next_value

    return total_sum


async def upper_text(text: str) -> str:
    """
    Преобразование текста в верхний регистр
    :param text: тест для преобразования
    :return: текст в верхнем регистре
    """
    return text.upper()
