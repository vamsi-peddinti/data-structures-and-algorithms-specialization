# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    maxratio=[]
    length=len(weights)
    for i in range(length):
        maxratio.append((values[i]/weights[i]))

    for j in range(len(maxratio)):
        max_value=max(maxratio)
        maxind=maxratio.index(max_value)
        if capacity%weights[maxind]>=0:
            capop=capacity//weights[maxind]
            value+=capop*values[maxind]
        capacity-=capop*weights[maxind]
        maxratio.remove(max_value)
        j+=1






    #print(maxratio, maxind)
    # write your code here
    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values, weights = [], []
    for i in range(n):
        a, b = map(int, input().split())
        values.append(a)
        weights.append(b)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
