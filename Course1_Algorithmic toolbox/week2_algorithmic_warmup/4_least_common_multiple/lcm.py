# Uses python3
import sys
def gcd_naive(a, b):
    if b==0:
        return a
    else:
        remainder=a%b
        return gcd_naive(b,remainder)


if __name__ == '__main__':
    a, b = map(int, input() .split())
    op=gcd_naive(a,b)
    print(int((a*b)/gcd_naive(a,b)))

