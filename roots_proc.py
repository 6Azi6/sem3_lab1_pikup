import math
import sys


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


def get_coefficients(arguments):
    names = ("A", "B", "C")
    return tuple(
        read_coefficient(name, arguments[index] if index < len(arguments) else None)
        for index, name in enumerate(names)
    )


def solve(a, b, c):
    discriminant = b * b - 4 * a * c

    if a == 0:
        if b == 0:
            return discriminant, [], c == 0
        squared_roots = [-c / b]
    elif discriminant < 0:
        squared_roots = []
    elif discriminant == 0:
        squared_roots = [-b / (2 * a)]
    else:
        square_root = math.sqrt(discriminant)
        squared_roots = [
            (-b - square_root) / (2 * a),
            (-b + square_root) / (2 * a),
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

    return discriminant, sorted(set(roots)), False


def main():
    a, b, c = get_coefficients(sys.argv[1:])
    discriminant, roots, infinitely_many = solve(a, b, c)

    print(f"Дискриминант: {discriminant:g}")
    if infinitely_many:
        print("Бесконечно много действительных корней")
    elif roots:
        print("Действительные корни: " + ", ".join(f"{root:g}" for root in roots))
    else:
        print("Действительных корней нет")


if __name__ == "__main__":
    main()
