from z3 import *

x = [[z3.Int("x_%s_%s" % (i, j)) for j in range(8)] for i in range(8)]

s = z3.Solver()

for j in range(7):
    for i in range(7):
        s.add(z3.Or(x[i][j] == z3.IntVal(0), x[i][j] == z3.IntVal(1)))

x[0][0] = 0
x[0][1] = 0
x[0][2] = 0
x[0][3] = 0
x[0][4] = 0
x[0][5] = 0

x[1][0] = 0
x[1][1] = 0
x[1][2] = 0
x[1][3] = 0
x[1][4] = 0
x[1][5] = 0

x[2][2] = 0
x[2][3] = 0
x[2][4] = 0
x[2][5] = 0

x[3][2] = 0
x[3][3] = 0
x[3][4] = 0

x[4][1] = 0
x[4][2] = 0
x[4][3] = 0
x[4][4] = 0
x[4][5] = 0
x[4][6] = 0
x[4][7] = 0

x[5][1] = 0
x[5][2] = 0
x[5][3] = 0
x[5][4] = 0
x[5][5] = 0
x[5][6] = 0
x[5][7] = 0

x[6][1] = 0
x[6][2] = 0
x[6][3] = 0
x[6][4] = 0
x[6][5] = 0
x[6][6] = 0
x[6][7] = 0

x[7][6] = 0
x[7][7] = 0

s.add(x[2][0] + x[2][1] == 1)
s.add(x[2][1] == 1)
s.add(x[2][1] + x[3][1] == 2)
s.add(x[3][1] == 1)
s.add(x[3][1] + x[3][0] + x[4][0] + x[5][0] == 2)
s.add(x[4][0] + x[5][0] + x[6][0] == 1)
s.add(x[5][0] + x[6][0] + x[7][0] + x[7][1] + x[7][2] == 2)
s.add(x[7][1] + x[7][2] + x[7][3] == 1)
s.add(x[7][2] + x[7][3] + x[7][4] == 1)
s.add(x[7][3] + x[7][4] + x[7][5] == 1)
s.add(x[7][4] + x[7][5] == 1)
s.add(x[7][5] == 1)

s.add(x[0][6] + x[1][6] == 1)
s.add(x[0][6] + x[1][6] + x[2][6] == 1)
s.add(x[1][6] + x[2][6] + x[3][6] + x[3][5] == 2)
s.add(x[3][5] == 1)
s.add(x[3][5] + x[3][6] == 2)
s.add(x[3][5] + x[3][6] + x[3][7] == 3)
s.add(x[3][6] + x[3][7] == 2)

s.add(x[3][7] == 0)
print(s.check())
