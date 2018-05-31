import matplotlib.pyplot as plt
import csv
import geo_distance


"""
f=open("argentinaa.dat")
for row in csv.reader(f):
    print(row)
"""

"""
f=open("airports.dat",encoding="utf8")
arg=open("argentina.dat",'a')
writer=csv.writer(arg)
for row in csv.reader(f):
    if row[3] == 'Argentina':
        writer.writerow(row)
"""
latitudes={}
longitudes={}
nombres={}
f=open("airports.dat",encoding="utf8")

for row in csv.reader(f):
    if row[3]=="Argentina":
        airport_id=row[0]
        nombres[row[2].lower()]=airport_id
        latitudes[airport_id]=float(row[6])
        longitudes[airport_id]=float(row[7])

print(nombres)
print(geo_distance.distance(latitudes[nombres['rosario']],longitudes[nombres['rosario']],latitudes[nombres['cordoba']],longitudes[nombres['cordoba']]),'km papu')
