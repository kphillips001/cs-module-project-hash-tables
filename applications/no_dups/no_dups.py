def no_dups(s):
    # Your code here
    # list = string split by spaces
    l = s.split(' ')
    # second list
    new_list = []

    for w in l:
        if w not in new_list:
            new_list.append(w)
    return ' '.join(new_list)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))