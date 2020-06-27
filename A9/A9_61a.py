from z3 import *

x = Int("x")
z = Int("z")

x = z3.IntVal(36)

s = z3.Solver()

a = x - z3.IntVal(2) * z3.IntVal(8) + z3.IntVal(1) == z
b = x - z3.IntVal(2) * z3.IntVal(8) - z3.IntVal(1) == z
c = x - z3.IntVal(8) + z3.IntVal(2) == z
d = x - z3.IntVal(8) - z3.IntVal(2) == z
e = x + z3.IntVal(8) + z3.IntVal(2) == z
f = x + z3.IntVal(8) - z3.IntVal(2) == z
g = x + z3.IntVal(2) * z3.IntVal(8) + z3.IntVal(1) == z
h = x + z3.IntVal(2) * z3.IntVal(8) - z3.IntVal(1) == z

s.add(z3.Or(a, z3.Or(b, z3.Or(c, z3.Or(d, z3.Or(e, z3.Or(f, z3.Or(g, h))))))))

o = z3.And(z3.IntVal(18) <= z, z3.IntVal(21) >= z)
p = z3.And(z3.IntVal(26) <= z, z3.IntVal(29) >= z)
q = z3.And(z3.IntVal(34) <= z, z3.IntVal(37) >= z)
r = z3.And(z3.IntVal(42) <= z, z3.IntVal(45) >= z)

s.add(z3.Or(o, z3.Or(p, z3.Or(q, r))))

s.check()
m = s.model()
print(m)
