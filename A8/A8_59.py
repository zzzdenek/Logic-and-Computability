# if we have two big numbers like a = 0x7FFF807E and b = 0x7FFF807E
# the sum reaches a overflow, if the most significant bit gets 1
# like in this example a + b = 0xFFF00FC
# therefore the if-clause is satisfied, the addition gets executed but
# but c >= 0 will not be satisfied

from z3 import *

a = z3.Int('a')
b = z3.Int('b')
c = z3.Int('c')

s = z3.Solver()

c = 0

c = z3.If(z3.And(a > 0, b > 0), a+b, c)

s.add(c < 0)

print(s.check())

a = z3.BitVec("a", 32)
b = z3.BitVec("b", 32)
c = z3.BitVec("c", 32)

s = z3.Solver()

c = 0

c = z3.If(z3.And(a > 0, b > 0), a+b, c)

s.add(c < 0)

print(s.check())

m = s.model()

a_val = m[a].as_long()
b_val = m[b].as_long()

print(m)
