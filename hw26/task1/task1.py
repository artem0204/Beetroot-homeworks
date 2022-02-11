def bubble_sort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True


if __name__ == "__main__":
    l = [5, 13, 2, 14, 77, 3, 10, 8, 78, 1]
    bubble_sort(l)
    print(l)

