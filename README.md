# PythonLibrary cheetsheet

cheetsheet

### csv を扱う

```
import re 
import csv

with open(csvfile,encoding="UTF-8") as f:
    for line in f:
        x = re.split('[,\n()]',line)

with open(csvfile, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["year", "80s","90s","00s","10s"])
```
