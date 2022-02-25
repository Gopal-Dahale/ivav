def hadamard_gate(index, vector, size):
    start = 0
    end = 2**index
    dist = end - start

    while start < size:
        last = start + dist
        a = vector[start]
        b = vector[last]
        vector[start] = a + b
        vector[last] = a - b
        start += 1
        if start == end:
            start = end + dist
            end = start + dist

    return vector
