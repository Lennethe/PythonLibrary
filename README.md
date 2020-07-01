# PythonLibrary cheetsheet

cheetsheet



## 読み込み書き込み

<details><summary> csv を読み込む </summary>

```
import re 
import csv

with open(csvfile,encoding="UTF-8") as f:
    for line in csv.reader(f):
        x = list(line)
```

</details>



<details><summary> csvを書き込む </summary>

```
with open(csvfile, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["year", "80s","90s","00s","10s"])
```

</details>


<details><summary> ファイルを読み込む </summary>

```
with open(file,encoding="UTF-8") as f:
    for line in f:
        x = re.split('[,\n()]',line)
```

</details>


<details><summary> ファイルを書き込む </summary>

```
with open(file, 'w') as f:
    f.write("\n")
```

</details>
