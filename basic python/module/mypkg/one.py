def pat(n):
    for var in range(n):
        for _ in range(n-var):
            print(" ",end='')
        for _ in range(var):
            print("*",end='')
        print()
if __name__ == '__main__':
    print("current file or module name :", __name__)
    n = int(input("Enter no of lines : "))
    pat(n)
