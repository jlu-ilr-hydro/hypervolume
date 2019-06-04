from ctypes import *
import os
class Hypervolume:

    def __init__(self):
        self.libCalc = CDLL(os.path.dirname(__file__) + "/libhvci.so")

    def __call__(self, pyarr):
        dim_y = len(pyarr)
        dim_x = len(pyarr[0])

        # TODO if no two dim array / list --> raise Error and explain

        # set C function "hvc" correct result type
        self.libCalc.hvc.restype = c_double
        self.libCalc.hvc.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]

        double_2dim_pointer = []
        for i, line_x in enumerate(pyarr):
            dim_x_arr = (c_double * len(line_x))(*line_x)
            double_2dim_pointer.append(dim_x_arr)

        dyn_arr = (POINTER(c_double) * len(pyarr))(*double_2dim_pointer)

        # call C "hvc" correct result type
        return self.libCalc.hvc(dyn_arr, dim_x, dim_y)