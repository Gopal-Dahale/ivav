"""Pauli X Gate"""


def pauli_x(index, vector, size):
    """Pauli's X gate

    Args:
        index (int): Index of the qubit to be flipped
        vector (list): State vector
        size (int): Size of the state vector
    """
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
