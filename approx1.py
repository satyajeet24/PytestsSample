from pytest import approx
import numpy as np

def findApproxValues():
    print("Eg 1 : ", end=" ")
    print(0.1 + 0.2 == approx(0.3))

    print("Eg 2 : ", end=" ")
    print((0.1 + 0.2, 0.3 + 0.5) == approx((0.3, 0.8)))

    print("Eg 3 : ", end=" ")
    print({'a': 0.1 + 0.2, 'b': 0.2 + 0.4} == approx({'a': 0.3, 'b': 0.6}))

    print("Eg 4 : ", end=" ")
    print(np.array([0.1, 0.2]) + np.array([0.3, 0.1]) == approx(np.array([0.4, 0.3])))

    print("Eg 5 : ", end=" ")
    print(np.array([0.1, 0.2]) + np.array([0.3, 0.1]) == approx(np.array([0.41, 0.31])))


findApproxValues()
