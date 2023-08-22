import argparse

def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    return result

def multiply_numbers(a, b):
    result = a * b
    print(f"The product of {a} and {b} is: {result}")
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculator')
    parser.add_argument('operation', choices=['add', 'multiply'], help='Choose the operation (add/multiply)')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')

    args = parser.parse_args()

    if args.operation == 'add':
        result = add_numbers(args.a, args.b)
    else:
        result = multiply_numbers(args.a, args.b)






# # Example usage
# num1 = 5
# num2 = 7
# result = add_numbers(num1, num2)
#
#
#
#
# if __name__ == '__main__':
