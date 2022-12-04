def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        return quick_sort([e for e in ls[1:] if e <= ls[0]]) + [ls[0]] +\
            quick_sort([e for e in ls[1:] if e > ls[0]])


def getSecondMax(ls):
    return ls[-2]


def main():
    lst = [43, 21, 65, 86, 54, 74, 24, 65, 11, 2, 21, 54, 75, 0]
    print(getSecondMax(quick_sort(lst)))


if(__name__=='__main__'):
    main()