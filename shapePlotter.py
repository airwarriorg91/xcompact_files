import csv
import pandas as pd
import matplotlib.pyplot as plt
datContent=[]

# read flash.dat to a list of lists
for i in open("./geo_shape.dat").readlines():
    l = i.strip().split()
    r = []
    for j in l:
        r.append(j)
    datContent.append(r)
print(datContent[0])

# write it as a new CSV file
with open("./geoshape.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)
    
    
df = pd.read_csv("geoshape.csv")
plt.scatter(df.x, df.y)
plt.xlim([7,9])
plt.ylim([7,9])
plt.show()
