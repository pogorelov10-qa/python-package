import sys
from more_itertools import sliced

def main():
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            # Пример логики: выводим результат вычислений
            result = n / 2  # или ваша логика
            print(result)
        except ValueError:
            print("Please provide an integer")
            sys.exit(1)
    else:
        print("Usage: hexlet-python-package <number>")
        sys.exit(1)

if __name__ == "__main__":
    main()