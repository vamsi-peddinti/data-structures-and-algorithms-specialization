# Uses python3
import sys

def get_change(m):
    total_coins=0
#  The following "//" is for quotient
# The following "%" is for remainder
    if m%10>0:
        total_coins=m//10
        rten=m%10
        if rten%5>0:
            total_coins+=rten//5
            rfive=m%5
            total_coins+=rfive//1
        else:
            total_coins+=rten//5
    else:
        total_coins=m//10


    return total_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
