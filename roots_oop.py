import math
import sys


class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            if self.b == 0:
                return [], self.c == 0
            squared_roots = [-self.c / self.b]
        elif self.discriminant < 0:
            squared_roots = []
        elif self.discriminant == 0:
            squared_roots = [-self.b / (2 * self.a)]
        else:
            square_root = math.sqrt(self.discriminant)
            squared_roots = [
                (-self.b - square_root) / (2 * self.a),
                (-self.b + square_root) / (2 * self.a),
            ]

        roots = []
        for value in squared_roots:
            if value < 0:
                continue
            if value == 0:
                roots.append(0.0)
            else:
                root = math.sqrt(value)
                roots.extend((-root, root))

        return sorted(set(roots)), False


def read_coefficient(name, argument):
    while True:
        value = argument if argument is not None else input(f"Введите {name}: ")
        argument = None

        try:
            number = float(value)
            if math.isfinite(number):
                return number
        except ValueError:
            pass

        print(f"Некорректный коэффициент {name}. Повторите ввод.")


def main():
    arguments = sys.argv[1:]
    coefficients = []
    for index, name in enumerate(("A", "B", "C")):
        argument = arguments[index] if index < len(arguments) else None
        coefficients.append(read_coefficient(name, argument))

    equation = BiquadraticEquation(*coefficients)
    roots, infinitely_many = equation.solve()

    print(f"Дискриминант: {equation.discriminant:g}")
    if infinitely_many:
        print("Бесконечно много действительных корней")
    elif roots:
        print("Действительные корни: " + ", ".join(f"{root:g}" for root in roots))
    else:
        print("Действительных корней нет")


if __name__ == "__main__":
    main()
