def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}  # store numbers
    result = []  # create list to store positive numbers
    for num in a:  # loop through each number
        cache[num] = num
        if num != 0 and -num in cache:  # if number is not 0 or negative number,
            result.append(abs(num))  # append absolute number to list of result

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
