def gen_bin_tree(hight, root, left_child = lambda x: x * 3 + 1, right_child = lambda x: x * 3 - 1) -> list|None:
    """
       Нерекурсивно строит бинарное дерево.

        Аргументы:
            height: Заданная высота
            root: Заданное значение корня
            left_child: Функция для вычисления левого потомка
            right_child: Функция для вычисления правого потомка
        Возвращает:
            Массив, представляющий бинарное дерево, или None, если дерева нет
    """
    if hight == 0:
        return None
    tree_size = 2**hight - 1
    t = [0] * tree_size
    t[0] = root
    for i in range(1, tree_size):
        if i % 2 != 0:
            p = (i - 1) // 2
            t[i] = left_child(t[p])
        else:
            p = (i - 2) // 2
            t[i] = right_child(t[p])
    return t


def print_tree(tree):
    """Красиво выводит дерево по уровн"""
    if tree is None:
        print(t)
    else:
        i = 1
        while 2**(i-1) - 1 < len(t):
            print(i, ":", tree[2**(i-1) - 1: 2**i - 1])
            i+=1


t = gen_bin_tree(5, 10, lambda x: x * 3 + 1, lambda x: x * 3 - 1)
print_tree(t)