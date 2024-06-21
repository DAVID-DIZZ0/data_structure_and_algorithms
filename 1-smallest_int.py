def get_smallest_integer(my_list):

    # smallest count from index 0
    smallest_num = my_list[0]


# iterating index of each element in the list

    for i in my_list:

        if i < smallest_num:

            smallest_num = i

# return value

    return smallest_num


if __name__ == "__main__":
    my_list=[2, 5, 23, 7, 1, 874]

    print(get_smallest_integer(my_list))
