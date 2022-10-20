import numpy as np
import numpy.linalg as la

a = [1, 2, 0]
b = [-4, 3, 4]
c = [-1, -6, 2]
d = [-1, 0, -8]

a = np.array(a)
b = np.array(b)
c = np.array(c)
d = np.array(d)

b = b - a
c = c - a
d = d - a
a = a - a

print("rebased vectors: ")
for v in [a, b, c, d]:
    print(v)

a1 = np.cross(b, c) / 2
a2 = np.cross(b, d) / 2
a3 = np.cross(c, d) / 2

bc = c - b
bd = d - b

a4 = np.cross(bc, bd) / 2

a = [a1, a2, a3, a4]

print("cross products: ")
for n in a:
    print(n)

s = 0

print("magnitudes: ")
for n in a:
    m = la.norm(n)

    s += m
    print(m)

print("surface area: ")
print(s)
