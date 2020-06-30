# PythonLibrary cheetsheet

cheetsheet

## ファイル読み込み
### csv を読み込む

```
import re 
import csv

with open(csvfile,encoding="UTF-8") as f:
    for line in f:
        x = re.split('[,\n()]',line)
```

### csv を書き込む
```
with open(csvfile, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["year", "80s","90s","00s","10s"])
```
### ファイル を書き込む
```
with open(csvfile, 'w') as f:
    f.write("\n")
```
