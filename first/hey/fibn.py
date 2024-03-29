import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The fibunacci number you wish to calcualte", type=int)
    args = parser.parse_args()
    result = fib(args.num)
    if args.num==0:
        print("The "+str(args.num)+ " fib number is "+str(result))

    elif args.num==1:
        print("The "+str(args.num)+ "st fib number is "+str(result))

    elif args.num==2:
        print("The "+str(args.num)+ "nd fib number is "+str(result))

    elif args.num<0:
        print("No minus")

    else:        
        print("The "+str(args.num)+ "th fib number is "+str(result))


if __name__ == '__main__':
    Main()