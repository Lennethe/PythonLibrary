# PythonLibrary cheetsheet

cheetsheet

## ファイル読み込み
### csv を読み込む

```
import re 
import csv

with open(csvfile,encoding="UTF-8") as f:
    for line in csv.reader(fr):
        x = list(line)
    for line in f:
        x = re.split('[,\n()]',line)
```

### csv を書き込む
```
with open(csvfile, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["year", "80s","90s","00s","10s"])
```

### ファイルを読み込む

```
with open(file,encoding="UTF-8") as f:
    for line in f:
        x = re.split('[,\n()]',line)
```

### ファイルを書き込む
```
with open(file, 'w') as f:
    f.write("\n")
```
