def find_unique(l):
    unq_list = []
    for i in range(len(l)):
        if l[i] not in l[i+1:]: 
            if l[i] not in unq_list: unq_list.append(l[i])

    return unq_list


if __name__ == "__main__":
    l = list(map(int, input("Enter list of numbers: ").split()))
    print("The distinct elements of list are", find_unique(l))
    print("The distinct elements of list are", list(set(l)))