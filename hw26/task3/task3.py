import statistics
def quick_sort(list_):
    len_list = len(list_)
    if len_list <= 1:
        return list_
    element = statistics.median([list_[0],list_[len_list//2],list_[len_list-1]])
    left = list(filter(lambda x:x<element,list_))
    right = list(filter(lambda x:x>element,list_))
    return quick_sort(left)+[element]+quick_sort(right)
if __name__ == "__main__":
    print(quick_sort([7, 6, 10, 5, 9, 8, 3, 4]))