def guess_num(t: int, mn: int, mx: int, sp: int):
    """
        Угадывает число в диапазоне используя бинарный поиск или медленный поиск.

        Аргументы:
            t: Загаданное число
            mn: Минимальное значение диапазона
            mx: Максимальное значение диапазона
            sp: Метод нахождения числа: медленный перебор(1) или бинарный поиск(2)

        Возвращает:
            Список содержащий:
            - Количество использованных попыток
            - Угаданное число если найдено, иначе None
    """
    if mn > mx:
        mn, mx = mx, mn
    if t < mn or t > mx:
        return [t, None]
    w = list(range(mn, mx+1))
    lw = len(w)
    if sp == 1:
        k = 0
        while w[k] != t:
            k += 1
        return [w[k], k + 1]
    else:
        ll = w[0] - 1
        rr = w[lw - 1]
        k = 0
        while rr - ll > 1:
            mm = (rr + ll) // 2
            if mm >= t:
                rr = mm
            else:
                ll = mm
            k += 1
        if k == 0:
            k += 1
        return [rr, k]


print(guess_num(4, 2, 6, 1))
