# PythonLibrary

cheetsheet

```
with open(csvfile,encoding="UTF-8") as f:
    for line in f:
        x = re.split('[,\n()]',line)
        print(x)
        year = x[0]
        decade = x[1]
        label = x[3]
        print(x)
        if year not in dic: dic[year] = {}
        dic[year][decade] = label

with open(csvfile, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["year", "80s","90s","00s","10s"])
    #writer.writerow(["year","all"])
    for k in sorted(list(dic.keys())):
        print(k)
        writer.writerow([k, dic[k]["80s"],dic[k]["90s"],dic[k]["00s"],dic[k]["10s"]])

```
