from z3 import *

w = z3.Int('w')
x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')

s = z3.Solver()

s.add(z3.IntVal(-9)*w - z3.IntVal(19)*x + z3.IntVal(4)*y - z3.IntVal(8)*z == z3.IntVal(-152))
s.add(z3.IntVal(-15)*w + z3.IntVal(10)*x + z3.IntVal(20)*y + z3.IntVal(14)*z == z3.IntVal(-115))
s.add(z3.IntVal(2)*w - z3.IntVal(20)*x + z3.IntVal(20)*y - z3.IntVal(12)*z == z3.IntVal(86))
s.add(z3.IntVal(-15)*w + z3.IntVal(18)*x + z3.IntVal(11)*y - z3.IntVal(10)*z == z3.IntVal(0))

s.check()
m = s.model()

w_val = m[w].as_long()
x_val = m[x].as_long()
y_val = m[y].as_long()
z_val = m[z].as_long()

print("w = ")
print(w_val)
print("x = ")
print(x_val)
print("y = ")
print(y_val)
print("z = ")
print(z_val)

