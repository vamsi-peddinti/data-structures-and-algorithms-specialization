def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_index1=0
    for first in range(n):
        if max_index1==0 or numbers[first]>numbers[max_index1]:
            max_index1=first
    max_index2=0
    for second in range(n):
        if second!=max_index1 and (max_index2==0 or numbers[second]>numbers[max_index2]):
            max_index2=second

    return  (numbers[max_index1] * numbers[max_index2])


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
