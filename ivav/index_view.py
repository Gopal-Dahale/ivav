from ivav.gates.single_qubit.pauli import x, y, z
from ivav.gates.single_qubit import h
from ivav.gates.multi_qubit.control import ccx, cx


class IndexView:

    def __init__(self, n, state_vector):
        self.n = n
        self.state_vector = state_vector
        self.len = len(state_vector)
        assert self.len == 2**n, "The state vector must be of length 2**n"

    def x(self, index):
        assert index < self.n, "Index must be less than n"
        self.vector = x.pauli_x(index, self.state_vector, self.len)

    # Yet to be implemented
    def y(self, index):
        self.vector = y.pauli_y(index, self.state_vector)

    # Yet to be implemented
    def z(self, index):
        self.vector = z.pauli_z(index, self.state_vector)

    def h(self, index):
        self.vector = h.hadamard_gate(index, self.state_vector, self.len)

    def cx(self, control, target):
        assert control < self.n, "Control index must be less than n"
        assert target < self.n, "Target index must be less than n"
        self.vector = cx.cx(control, target, self.state_vector, self.n)

    def ccx(self, control1, control2, target):
        assert control1 < self.n, "Control1 index must be less than n"
        assert control2 < self.n, "Control2 index must be less than n"
        assert target < self.n, "Target index must be less than n"
        self.vector = ccx.ccx(control1,control2,target, self.state_vector,self.n)