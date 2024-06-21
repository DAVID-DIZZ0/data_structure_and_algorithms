def find_first_occurence(my_list, num):

    for i in range(len(my_list)):

        if my_list[i] == num:

            # return the value after iteration

            return i

# return statement if the elements in list does not exist

    return -1

if __name__ == "__main__":
    print(find_first_occurence([4,6,8,2,5,3],6))
