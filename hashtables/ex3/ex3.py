def intersection(arrays):
    dict = {}
    shortestArray = None
    result = []

    for arr in arrays:
        if shortestArray == None or len(arr) < len(shortestArray):
            shortestArray = arr

        for num in arr:
            # here we are setting the number as the key,
            # and the value as the number of times this
            # particular number has appeared
            if num in dict:
                # key is the num, value is the count
                # ie # of times the num has appeared
                dict[num] += 1
            else:
                # this is the first time the num has
                # appeared, so you just set it to count 1
                dict[num] = 1

            # if the count is the same as the number of arrays,
            # we know the number has appeared in each array,
            # and so it is an intersecting integer
            if dict[num] == len(arrays):
                result.append(num)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])


    print(intersection(arrays))
