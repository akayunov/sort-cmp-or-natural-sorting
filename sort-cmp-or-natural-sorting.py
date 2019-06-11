def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def mycmp(x, y):
    if len(x) != len(y):
        return 1 if len(x) > len(y) else -1
    else:
        return 1 if x > y else (0 if x == y else -1)


print(sorted(['qwe1', 'qwe212', 'qwe414', 'qwe3']))
print(sorted(['qwe1', 'qwe212', 'qwe414', 'qwe3'], key=cmp_to_key(mycmp)))
