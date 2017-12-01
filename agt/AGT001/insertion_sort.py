import random

# insertion sort T=O(n^2)
# origin = [4,5,2,7]
# init : origin = [4,5,2,7] new = [4]
#        origin = [4,->5,2,7] new = [4,5]
#        origin = [4,5,->2,7] new = [2,4,5]
#        origin = [4,5,2,->7] new = [2,4,5,7]
#
# update with python3


def insert_sort(unsorted_list):
    new_list = [unsorted_list[0]]
    for num in unsorted_list[1:]:
        flag = 0
        for index, position in enumerate(new_list):
            if num <= position:
                flag = 1   # cause last number in new_list,use break can not easy get the index
                break
        if flag:
            new_list.insert(index, num)
        else:
            new_list.append(num)

    return new_list


if __name__ == "__main__":
    unsorted_list = [random.randint(1, 10) for _ in range(10)]
    print(unsorted_list)
    sorted_list = insert_sort(unsorted_list)
    print(sorted_list)
    
