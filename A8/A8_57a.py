from z3 import *

w = z3.Int('w')
x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')

s = z3.Solver()

s.add(z3.IntVal(-18)*w - z3.IntVal(7)*x + z3.IntVal(3)*y + z3.IntVal(2)*z == z3.IntVal(-137))
s.add(z3.IntVal(7)*w - z3.IntVal(18)*x + z3.IntVal(15)*y + z3.IntVal(20)*z == z3.IntVal(410))
s.add(z3.IntVal(17)*w + x - z3.IntVal(20)*y - z3.IntVal(5)*z == z3.IntVal(389))
s.add(z3.IntVal(-2)*w + z3.IntVal(2)*x + z3.IntVal(2)*y + z3.IntVal(6)*z == z3.IntVal(-50))

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
