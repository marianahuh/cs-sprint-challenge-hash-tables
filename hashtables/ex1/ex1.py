def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    if length <= 1:  # if input is less than 2 entries, return None
        return None
    for idx in range(length):  # loop to get indicies in list
        key_idx = weights[idx]  # assign weight as key
        if key_idx in cache:  # if key is in cache,
            val_idx = cache[key_idx]  # assign weight index as value
            return (idx, val_idx)  # return index and value
        cache[limit - weights[idx]] = idx  # calculate and add to cache

    return None


weights = [4]
print(get_indices_of_item_weights(weights, 1, 4))
weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21))
weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights, 9, 21))
