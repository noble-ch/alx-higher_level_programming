def all_equal(lists):
    if len(lists) <= 1:
        return True
    for i in range(1 , len(lists)):
        if lists[0]  == lists[i]:
            return True
        else:
            return False


print(all_equal([3, 3, 3, 3, 3, 2, 3]))