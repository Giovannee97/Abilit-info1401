import math
import numpy

import numpy as np
coord = np.loadtxt("ex2_data_python_4.txt", dtype='f', delimiter=None)

print("Matrice delle coordinate:")
print(coord)

x=[]

x.append(((1.0/len(coord))*coord.sum(axis=0)))

print("Le coordinate del Baricentro sono:",x[0])
