def mean(l):
    return round(sum(l) / len(l), 4)

def median(l):
    sorted_list = sorted(l)
    if len(sorted_list) % 2:
        return sorted_list[((len(sorted_list) + 1) // 2) - 1]
    else:
        m1 = (len(sorted_list) // 2) - 1
        m2 = (len(sorted_list) // 2)

        return (sorted_list[m1] + sorted_list[m2]) / 2

def mode(l):
    dic = {}
    for x in l:
        if x in dic.keys(): dic[x] += 1
        else: dic[x] = 1

    maxKey = max(dic, key = lambda m: dic[m])

    return maxKey


if __name__ == "__main__":
    l = list(map(int, input("Enter list of numbers: ").split()))
    print("The mean is", mean(l))
    print("The median is", median(l))
    print("The mode is", mode(l))
