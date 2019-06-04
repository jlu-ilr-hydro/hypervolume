-----------------------------------------------------------------
                    Computation of the Hypervolume

        Carlos M. Fonseca, Manuel López-Ibáñez and Luís Paquete
-----------------------------------------------------------------




# Introduction


This program implements a recursive, dimension-sweep algorithm for
computing the hypervolume indicator of the quality of a set of n
non-dominated points in d dimensions. It also incorporates a
recent result for the three-dimensional special case. The proposed
algorithm achieves O(n^{d-2} log n) time and linear space complexity
in the worst-case, but experimental results show that the pruning
techniques used may reduce the time complexity even further.

Rewritten for python by @bees4ever.

Relevant literature:

[1] Carlos M. Fonseca, Luís Paquete, and Manuel López-Ibáñez. An
    improved dimension-sweep algorithm for the hypervolume
    indicator. In IEEE Congress on Evolutionary Computation, pages
    1157-1163, Vancouver, Canada, July 2006.

[2] Nicola Beume, Carlos M. Fonseca, Manuel López-Ibáñez, Luís
    Paquete, and J. Vahrenhold. On the complexity of computing the
    hypervolume indicator. IEEE Transactions on Evolutionary
    Computation, 13(5):1075-1082, 2009.



# Building

To generate a python readable hypervolume library, on can run 

`gcc -shared -o libhvci.so -fPIC hvc.c hv.c timer.c avl.c`

Using the defined setup will do this for you on Linux / Unix Systems (Mac OS)

``python setup.py build``
