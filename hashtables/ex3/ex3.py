def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}  # store numbers
    result = []  # store intersected numbers in result list
    nums = len(arrays)
    for num_list in arrays:  # loop through each list in each array
        for elm in num_list:  # loop through each element in list
            if elm not in cache:  # if element is not in cache, store to cache
                cache[elm] = 1
            else:
                # otherwise, if it is in cache increment element by 1
                cache[elm] += 1
                if cache[elm] == nums:  # if elements in cache equals total amount in nums,
                    result.append(elm)  # append the elements to result list

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
