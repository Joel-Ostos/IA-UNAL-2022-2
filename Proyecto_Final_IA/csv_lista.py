import os
import menu
from menu import archivo

a = str(archivo)

b = a.split()
rows, cols = [], []

count = 0
firstlen = 0
for lst in b:
    elems = lst.split(",")
    if firstlen == 0:
        firstlen = len(elems)
    if len(elems) < firstlen:
        rows.append(elems)
    else:
        cols.append(elems)


for lst in rows:
    while '' in lst:
        lst.remove('')
for lst in cols:
    while '' in lst:
        lst.remove('')

for i in range(len(rows)):
    rows[i] = [int(a) for a in rows[i]]

for i in range(len(cols)):
    cols[i] = [int(a) for a in cols[i]]

print(f"cols = {cols}")
print(f"rows = {rows}")
