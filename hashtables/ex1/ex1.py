
# Naive solution just for practice

# def get_indices_of_item_weights(weights, length, limit):
#     for i in range(0, length):
#         for j in range(i + 1, length):
#             if (weights[i] + weights[j] == limit):
#                 print((i, j))


# print(get_indices_of_item_weights([0, 1, 2, 3, 4, 5, 6], 7, 4))

# hash solution

def get_indices_of_item_weights(weights, length, limit):
    # arrays with only 1 value should return None
    if length < 2:
        return None
    # create an empty hash table
    dict = {}
    # for each item in array
    for i, item in enumerate(weights):
        # check if pair exists
        # if difference has been seen before, print the pair
        if (limit - item) in dict:
            # order was specified - greater index first,
            # then lesser index
            if i > dict[limit - item]:
                return (i, dict.get(limit - item))
            else:
                return (dict.get(limit - item), i)
        else:
        # store index of current element in dict
            dict[item] = i
