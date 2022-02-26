"""Index View Module"""
import numpy as np
from ivav.gates.single_qubit.pauli import x, y, z
from ivav.gates.single_qubit import h
from ivav.gates.multi_qubit.control import ccx, cx


class IndexView:
    """Index View class
    """

    def __init__(self, n, state_vector) -> None:
        """Init function to initialize the IndexView class

        Args:
            n (int): Number of qubits
            state_vector (list): SState vector representeing the states of the qubits
        """
        self.n = n
        self.state_vector = np.array(state_vector, dtype=np.float32)
        self.len = len(state_vector)
        assert self.len == 2**n, "The state vector must be of length 2**n"

    def x(self, index):
        """Not gate

        Args:
            index (int): Index of the qubit to be flipped
        """
        assert index < self.n, "Index must be less than n"
        x.pauli_x(index, self.state_vector, self.len)

    # Yet to be implemented
    def y(self, index):
        """Y gate

        Args:
            index (int): Index of the qubit to which the gate is applied
        """
        y.pauli_y(index, self.state_vector)

    # Yet to be implemented
    def z(self, index):
        """Z Gate

        Args:
            index (int): Index of the qubit to which the gate is applied
        """
        z.pauli_z(index, self.state_vector)

    def h(self, index):
        """Hadamard gate

        Args:
            index (int): Index of the qubit to which the gate is applied
        """
        h.hadamard_gate(index, self.state_vector, self.len)

    def cx(self, control, target):
        """Controlled Not gate

        Args:
            control (int): Control bit
            target (int): Target bit
        """
        assert control < self.n, "Control index must be less than n"
        assert target < self.n, "Target index must be less than n"
        cx.cx(control, target, self.state_vector, self.n)

    def ccx(self, control1, control2, target):
        """Controlled Controlled Not gate

        Args:
            control1 (int): Control bit 1
            control2 (int): Control bit 2
            target (int): Target bit
        """
        assert control1 < self.n, "Control1 index must be less than n"
        assert control2 < self.n, "Control2 index must be less than n"
        assert target < self.n, "Target index must be less than n"
        self.state_vector = ccx.ccx(control1, control2, target,
                                    self.state_vector, self.n)
