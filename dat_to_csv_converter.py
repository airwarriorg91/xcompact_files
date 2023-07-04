import csv

datContent=[['Time','Lift','Drag']]

# read flash.dat to a list of lists
for i in open("./forces.dat").readlines():
    l = i.strip().split()
    r = []
    for j in l:
        r.append(j)
    datContent.append(r)

# write it as a new CSV file
with open("./forces.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)