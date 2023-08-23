import argparse


def add_numbers(a, b):
    """
    Adds two numbers together.
    :param a: The first number.
    :param b: The second number.
    :return: The sum of the two numbers.
    """
    return a + b


def multiply_numbers(a, b):
    """
    Multiplies two numbers.
    :param a: The first number.
    :param b: The second number.
    :return: The product of the two numbers.
    """
    return a * b




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculator')
    parser.add_argument('operation', choices=['add', 'multiply'],
                        help='Choose the operation (add/multiply)')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')

    args = parser.parse_args()

    # Perform the chosen operation
    if args.operation == 'add':
        result = add_numbers(args.a, args.b)
        print(f"The sum of {args.a} and {args.b} is: {result}")
    else:
        result = multiply_numbers(args.a, args.b)
        print(f"The product of {args.a} and {args.b} is: {result}")

