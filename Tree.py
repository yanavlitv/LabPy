def build(pos, left, right, value, tree, current_height, max_hight, root):
    """
       Рекурсивно строит бинарное дерево.

       Аргументы:
           pos: Текущая позиция в массиве
           left: Левый индекс диапазона
           right: Правый индекс диапазона
           value: Текущее значение узла
           tree: Массив для хранения дерева
           current_height: Текущая высота
           max_height: Максимальная высота дерева
           root: Корневое значение
    """
    if right - left == 1:
        tree[pos] = value
        return
    else:
        tree[pos] = root
    middle = (right + left) // 2
    build(2*pos + 1, left, middle, root*3+1, tree, current_height+1, max_hight, root*3+1)
    build(2*pos + 2, middle + 1, right, root*3-1, tree, current_height+1, max_hight, root*3-1)
    return


def gen_bin_tree(height = 5, root = 10):
    """
        Запускает функцию build на заданных параметрах.

        Аргументы:
            height: Заданная высота
            root: Заданное значение корня
        Возвращает:
            Массив, представляющий бинарное дерево
    """
    t = [0] * (2**height - 1)
    build(0, 0, 2**height - 1, 0,  t, 1, height, root)
    return t

print(gen_bin_tree(5, 10))







