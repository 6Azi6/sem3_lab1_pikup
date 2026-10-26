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


def roots_from_squared(value):
    if value < 0:
        return ()
    if value == 0:
        return (0.0,)

    root = math.sqrt(value)
    return (-root, root)


def solve(a, b, c):
    discriminant = b * b - 4 * a * c

    if a == 0:
        if b == 0:
            return discriminant, ("infinite",) if c == 0 else ("none",)
        squared_roots = (-c / b,)
    elif discriminant < 0:
        squared_roots = ()
    elif discriminant == 0:
        squared_roots = (-b / (2 * a),)
    else:
        square_root = math.sqrt(discriminant)
        squared_roots = (
            (-b - square_root) / (2 * a),
            (-b + square_root) / (2 * a),
        )

    roots = tuple(sorted(set(
        root for value in squared_roots for root in roots_from_squared(value)
    )))
    return discriminant, ("roots", roots) if roots else ("none",)


def print_result(result):
    match result:
        case ("infinite",):
            print("Бесконечно много действительных корней")
        case ("roots", roots):
            print("Действительные корни: " + ", ".join(f"{root:g}" for root in roots))
        case ("none",):
            print("Действительных корней нет")


def main():
    arguments = sys.argv[1:]
    a, b, c = (
        read_coefficient(name, arguments[index] if index < len(arguments) else None)
        for index, name in enumerate(("A", "B", "C"))
    )
    discriminant, result = solve(a, b, c)

    print(f"Дискриминант: {discriminant:g}")
    print_result(result)


if __name__ == "__main__":
    main()
