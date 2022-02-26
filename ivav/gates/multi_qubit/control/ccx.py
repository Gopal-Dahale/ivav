"""Controlled Contrelled Not gate"""


def ccx(control1, control2, target, vector, n):
    num = 2**(n - 3)
    pos1 = ['0'] * n
    for i in range(num):
        k = bin(i)[2:]
        m = 0
        for j in range(n):
            if j == control1 or j == control2:
                pos1[j] = '1'
            elif j == target:
                pos1[j] = '0'
            else:
                pos1[j] = k[m]
                m += 1
        pos2 = pos1.copy()
        pos2[target] = '1'
        pos1.reverse()
        pos2.reverse()
        x = int(''.join(pos1), 2)
        y = int(''.join(pos2), 2)
        vector[x], vector[y] = vector[y], vector[x]

    return vector
