import math
import sys


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)


def write_line(*elements):
    for i, element in enumerate(elements):
        if i != 0:
            sys.stdout.buffer.write(b"\t")
        if isinstance(element, float):
            element = "{0:0.3f}".format(element)
        print(element, end="")
    print()


# Quelques fonctions données d'avance


def f1(x):
    return (x - 31) * (x + 2) * (x + 4)


def f2(x):
    return math.sin(math.pi * (x - 4) / 16) * (x - 16) + 1


"""
Ecrivez votre programme à la suite de ce commentaire
"""


write_line("x", "f1")
for i in range(320):
    x = i / 10
    write_line(x, f1(x))
