# PythonLibrary cheetsheet

cheetsheet




<details><summary> 読み込み書き込み </summary>

<details><summary> csv を読み込む </summary>

```
import re 
import csv

with open(csvfile,encoding="UTF-8") as f:
    for line in csv.reader(f):
        x = list(line)
```

</details>
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



## 距離尺度

<details><summary> コサイン類似度 </summary>

```
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
```

</details>

## クラスタリング 

<details><summary> コサイン類似度 </summary>

```
from sklearn.manifold import TSNE
TSNE(n_components=2, random_state=0).fit_transform(all_array)
```

</details>

