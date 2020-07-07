# PythonLibrary cheetsheet

cheetsheet

<details><summary> テンプレ </summary>
<details><summary> サブテンプレ </summary>

```
```

</details>
</details>


## 入出力関係

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

</details>


<details><summary> ファイルパス参照 </summary>
<details><summary> 現在パスにあるフォルダ一覧 </summary>

```
import os
os.listdir(os.getcwd())
```

</details>
</details>


## 距離尺度

<details><summary> コサイン類似度 </summary>

```
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
```

</details>

## クラスタリング 

<details><summary> TSNE </summary>

```
from sklearn.manifold import TSNE
TSNE(n_components=2, random_state=0).fit_transform(all_array)
```

</details>

## プロットする時


<details><summary> 二次元上にラベルとともにプロットする時 </summary>

```
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

for v,label,name in zip(vectors,labels,names):
    plt.plot(v[0],v[1],'o')
    print(name,label)
    plt.annotate(name, xy=(v[0],v[1]))
plt.show()
pp = PdfPages("clustering.pdf")
pp.savefig()
pp.close()
```

</details>
