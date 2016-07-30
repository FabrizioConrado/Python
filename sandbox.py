import MyLib as L
import csv

# p1 = L.Person('Fab','36','UK')
# p2 = L.Person('Raq','33','BRA')
# p3 = L.Person('Bo','29','FRA')
#
#
# for item in L.Person._all:
#     print(item.name, item.age)


DataSource = [['Sales','12','24000'],
              ['Cost','12','20000'],
              ['Interest','12','450']]

p = []
for row in DataSource:
    p.append(L.Person(row[0],int(row[1]),int(row[2]),''))

for r in p:
    r.total = r.age * r.country

for r in p:
    print(r.name + ' total is ' + str(r.total))