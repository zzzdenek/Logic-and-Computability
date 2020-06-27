from z3 import *

a = z3.Real('a')
b = z3.Real('b')
c = z3.Real('c')

s = z3.Solver()

s.add(a > z3.RealVal(0), b > z3.RealVal(0), c > z3.RealVal(0))
s.add(a*b*c == z3.RealVal(72))
s.add(a+b+c == z3.RealVal(14))
s.add(a - b > z3.RealVal(0))
s.add(b - c > z3.RealVal(0))

s.check()
m = s.model()

a_val = m[a]
b_val = m[b]
c_val = m[c]

print("a = ")
print(a_val)
print("b = ")
print(b_val)
print("c = ")
print(c_val)
