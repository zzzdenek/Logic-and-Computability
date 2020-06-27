from z3 import *

u = z3.Int('u')
v = z3.Int('v')
w = z3.Int('w')
x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')

s = z3.Solver()

s.add(z3.IntVal(3)*u - z3.IntVal(16)*v + z3.IntVal(6)*w + z3.IntVal(5)*x + z3.IntVal(11)*y - z3.IntVal(10)*z == z3.IntVal(91))
s.add(z3.IntVal(-10)*u + z3.IntVal(14)*v - z3.IntVal(12)*w + z3.IntVal(19)*x + z3.IntVal(13)*y + z3.IntVal(6)*z == z3.IntVal(379))
s.add(z3.IntVal(-4)*u - z3.IntVal(16)*v - z3.IntVal(4)*x - z3.IntVal(16)*y - z3.IntVal(16)*z == z3.IntVal(-100))
s.add(z3.IntVal(-8)*u + z3.IntVal(17)*v - z3.IntVal(8)*w - z3.IntVal(12)*x - z3.IntVal(14)*y + z3.IntVal(8)*z == z3.IntVal(-29))
s.add(z3.IntVal(5)*u - z3.IntVal(7)*v - z3.IntVal(12)*w + z3.IntVal(13)*x - y - z3.IntVal(5)*z == z3.IntVal(124))
s.add(z3.IntVal(4)*u - z3.IntVal(10)*v + z3.IntVal(8)*w - z3.IntVal(8)*x + z3.IntVal(19)*y + z3.IntVal(4)*z == z3.IntVal(252))

s.check()
m = s.model()

u_val = m[u].as_long()
v_val = m[v].as_long()
w_val = m[w].as_long()
x_val = m[x].as_long()
y_val = m[y].as_long()
z_val = m[z].as_long()

print("u = ")
print(u_val)
print("v = ")
print(v_val)
print("w = ")
print(w_val)
print("x = ")
print(x_val)
print("y = ")
print(y_val)
print("z = ")
print(z_val)

