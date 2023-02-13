import argparse #สำหรับ รับ input จากภายนอก

def parse_input():
    parser = argparse.ArgumentParser(description='test program to learn about argparse')
    # parser.add_argument(
    #     'm', 
    #     type=int,
    #     help='value of M positional argument')

    # parser.add_argument(
    #     'n', 
    #     type=int,
    #     help='value of M positional argument')

    parser.add_argument(
        '--x', 
        type=int,
        required=True,
        help='value of x')

    parser.add_argument(
        '--yval',
        type=int,
        default=3,
        help='value of y')

    args = parser.parse_args()
    return args

def print_other():
    print('something else')

def print_ones():
    print('1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 ')

if __name__ == "__main__":
    x = parse_input()
    print_ones()
    print_other()
    print_ones()

    print(f'YVAL = {x.yval}')
    print(f'x = {x.x}')
    # print(f'm = {x.m}')
    # print(f'n = {x.n}')

# 






#if __name__ == "__main__":

    # args = parse_input()
    
    # x = args.x
    # y = args.yval
    # print(f'M = {args.m}')
    # print(f'calculate {x} x {y} = {x*y}')