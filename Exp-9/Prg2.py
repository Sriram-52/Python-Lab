def find_duplicates(l):
    dup_list = []
    for i in range(len(l)):
        if l[i] in l[i+1:]: 
            if l[i] not in dup_list: dup_list.append(l[i])

    return dup_list


if __name__ == "__main__":
    l = list(map(int, input("Enter list of numbers: ").split()))
    print("The duplicates of list are", find_duplicates(l))