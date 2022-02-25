def pauli_x(index, vector, size):
    start = 0
    end = 2**index
    dist = end - start

    while start < size:
        last = start + dist
        vector[start], vector[last] = vector[last], vector[start]
        start += 1
        if start == end:
            start = end + dist
            end = start + dist

    return vector