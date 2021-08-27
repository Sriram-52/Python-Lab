from functools import reduce

def cumalative_product(l, i):
    return reduce(lambda x, y: x * y, l[:i+1], 1)

if __name__ == "__main__":
    l = list(map(int, input("Enter list of nums: ").split()))
    cum_list = []
    for i in range(len(l)):
       cum_list.append(cumalative_product(l, i))
    
    print(cum_list)