if __name__ == "__main__":
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    mutations_allowed = 2
    flag = True

    for i in range(0, max(len(str1), len(str2))):
        if str1[i] != str2[i]: mutations_allowed -= 1

        if mutations_allowed <= 0:
            flag = False
            break
    
    if flag:
        print("Strings are nearly equal")
    else:
        print("Strings are not nearly equal")
