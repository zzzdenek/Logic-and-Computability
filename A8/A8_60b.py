from z3 import *

x = [[z3.Int("x_%s_%s" % (i+1, j+1)) for j in range(4)] for i in range(4)]
z = z3.Int("z")

s = z3.Solver()

s.add(z > 0)

for i in range(4):
    s.add(x[i][0] + x[i][1] + x[i][2] + x[i][3] == z)

for j in range(4):
    s.add(x[0][j] + x[1][j] + x[2][j] + x[3][j] == z)

s.add(x[0][0] + x[1][1] + x[2][2] + x[3][3] == z)
s.add(x[3][0] + x[2][1] + x[1][2] + x[0][3] == z)

y = []
for i in range(4):
    for j in range(4):
        y.append(x[i][j])

s.add(z3.Distinct(y))

s.check()
m = s.model()

for i in range(4):
    x_val0 = m[x[i][0]].as_long()
    x_val1 = m[x[i][1]].as_long()
    x_val2 = m[x[i][2]].as_long()
    x_val3 = m[x[i][3]].as_long()
    print("%s | %s | %s | %s\n" % (x_val0, x_val1, x_val2, x_val3))