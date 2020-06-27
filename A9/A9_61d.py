from z3 import *

x = [z3.Int("x_%s" % (i+1)) for i in range(16)]

s = z3.Solver()

o = z3.And(z3.IntVal(18) <= x[0], z3.IntVal(22) >= x[0])
p = z3.And(z3.IntVal(26) <= x[0], z3.IntVal(30) >= x[0])
q = z3.And(z3.IntVal(34) <= x[0], z3.IntVal(38) >= x[0])
r = z3.And(z3.IntVal(42) <= x[0], z3.IntVal(46) >= x[0])
t = z3.And(z3.IntVal(50) <= x[0], z3.IntVal(54) >= x[0])

s.add(z3.Or(o, z3.Or(p, z3.Or(q, z3.Or(r, t)))))

for i in range(15):
    a = x[i] - z3.IntVal(2) * z3.IntVal(8) + z3.IntVal(1) == x[i+1]
    b = x[i] - z3.IntVal(2) * z3.IntVal(8) - z3.IntVal(1) == x[i+1]
    c = x[i] - z3.IntVal(8) + z3.IntVal(2) == x[i+1]
    d = x[i] - z3.IntVal(8) - z3.IntVal(2) == x[i+1]
    e = x[i] + z3.IntVal(8) + z3.IntVal(2) == x[i+1]
    f = x[i] + z3.IntVal(8) - z3.IntVal(2) == x[i+1]
    g = x[i] + z3.IntVal(2) * z3.IntVal(8) + z3.IntVal(1) == x[i+1]
    h = x[i] + z3.IntVal(2) * z3.IntVal(8) - z3.IntVal(1) == x[i+1]

    s.add(z3.Or(a, z3.Or(b, z3.Or(c, z3.Or(d, z3.Or(e, z3.Or(f, z3.Or(g, h))))))))

    o = z3.And(z3.IntVal(18) <= x[i+1], z3.IntVal(22) >= x[i+1])
    p = z3.And(z3.IntVal(26) <= x[i+1], z3.IntVal(30) >= x[i+1])
    q = z3.And(z3.IntVal(34) <= x[i+1], z3.IntVal(38) >= x[i+1])
    r = z3.And(z3.IntVal(42) <= x[i+1], z3.IntVal(46) >= x[i+1])
    t = z3.And(z3.IntVal(50) <= x[i+1], z3.IntVal(54) >= x[i+1])

    s.add(z3.Or(o, z3.Or(p, z3.Or(q, z3.Or(r, t)))))

s.add(z3.Distinct(x))

s.check()

m = s.model()
print(m)
