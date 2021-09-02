def nearly_equal(a, b):
    if(len(a) != len(b) and len(a) != len(b)-1):
        return False
    al = a
    l = []
    count = 0
    x = 0
    a = a.lower()
    b = b.lower()
    for i in range(len(al)):
        if(a[i] == b[i]):
            l.append(a[i])
        elif(a[i] != b[i]):
            if(a[i] == b[i+1] and count <= 1):
                l.append(a[i])
            else:
                x = x+1
                break
            if(count <= 1):
                count = count+1
        else:
            l.append(b[i])
            break
    string = ("").join(l)
    print(string)
    if x == 0:
        return True
    return False


if __name__ == "__main__":
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    if nearly_equal(str1, str2):
        print("Strings are nearly equal")
    else:
        print("Strings are not nearly equal")
