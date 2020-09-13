# PythonLibrary cheetsheet

cheetsheet

<details><summary> テンプレ </summary>
<details><summary> サブテンプレ </summary>

```
```

</details>
</details>

### 例外処理

<details><summary> 例外処理 </summary>
<details><summary> 基本 </summary>

```
try:
    hoge
except NotADirectoryError:
    print("error")

```

</details>
</details>



### 入出力関係

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


<details><summary> 入力されたパス以下にあるファイルを全て参照する </summary>

```
def get_all_files(path):
    res = []
    try:
        tales = os.listdir(path)
        for tale in tales:
            res.extend(get_all_files(path+"/"+tale))
    except NotADirectoryError:
        res.append(path)
    return res
```

</details>


</details>


### 距離尺度

<details><summary> コサイン類似度 </summary>

```
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
```

</details>

### クラスタリング 

<details><summary> TSNE </summary>

```
from sklearn.manifold import TSNE
TSNE(n_components=2, random_state=0).fit_transform(all_array)
```

</details>

### プロットする時


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

<details><summary> 3次元グラフをアニメーションとして保存したい時 </summary>

```
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def render_frame(x, y, z, angle):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.view_init(30, angle)
    plt.close()
    # 軸の設定
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    # PIL Image に変換
    buf = BytesIO()
    fig.savefig(buf, bbox_inches='tight', pad_inches=0.0)
    return Image.open(buf)

images = [render_frame(angle) for angle in range(360)]
images[0].save('output.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

```

</details>
