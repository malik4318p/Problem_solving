def merge_the_tools(string, k):
    length = len(string)
    # substring_length = length//k
    number_of_substrings = length//k
    if length % k != 0:
        number_of_substrings += 1

    starting_index = 0
    # substring_length=k
    ending_index = k
    for i in range(number_of_substrings):
        printed_arr = ""
        dummy_string = string[starting_index:ending_index]
        for j in range(starting_index, ending_index):
            if string[j] not in printed_arr:
                printed_arr += string[j]
        print(printed_arr)
        starting_index += k
        ending_index += k
        if ending_index > length:
            ending_index = length


if __name__ == '__main__':
    string, k = input("enter the string : "), int(
        input("enter the number of substrings : "))
    merge_the_tools(string, k)
